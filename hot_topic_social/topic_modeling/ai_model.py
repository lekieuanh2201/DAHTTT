import os
import string
import re

from unidecode import unidecode
from elasticsearch import Elasticsearch
from pyspark.sql import SparkSession
from gensim.models.ldamodel import LdaModel
import gensim.corpora as corpora
import pandas as pd
from vncorenlp import VnCoreNLP


data_dir = '../data/'
es = None
spark = None
rdrsegmenter = None
stop_words = []

def clean_text(text):
    text = re.sub(r'[^\w\s]', r'', str(text))
    text = re.sub(r'\n', r' ', text)
    text = re.sub(r' +', r' ', text)
    text = text.strip().lower()
    return text

def normalize_index(txt: str)->str:
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to remove punctuation
    rs = txt.translate(translator)
    rs = unidecode(rs).strip()
    rs = rs.replace(' ', '_')
    return rs.lower()

def sent_to_words(sentences):
    for sentence in sentences:
        yield(sentence.split(' '))

def remove_stopwords(texts, stop_words):
    return [[word for word in doc if word not in stop_words] for doc in texts]

def make_bigram(texts):
    for text in texts:
        new_text = text
        for i in range(len(text)-1):
            bigram = text[i] + ' ' + text[i+1]
            new_text.append(bigram)
        yield(new_text)

def format_topics_sentences(ldamodel, corpus, ids):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row[0], key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = "+".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(ids)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)


def load():
    global es, spark, rdrsegmenter, stop_words
    es = Elasticsearch("http://localhost:9200")
    spark = SparkSession.builder \
        .appName("YourAppName") \
        .config("spark.driver.memory", "2g") \
        .config("spark.executor.memory", "2g") \
        .getOrCreate()
    rdrsegmenter = VnCoreNLP("topic_modeling\\vncorenlp\\VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')
    with open('topic_modeling\\vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line[:-1])
    
    df = None
    for file in os.listdir(data_dir):
        f_path = os.path.join(data_dir, file)
        if df == None:
            df = spark.read.option("encoding", "utf-8").json(f_path)
        else:
            new_df = spark.read.option("encoding", "utf-8").json(f_path)
            df = df.union(new_df)
    rdd = df.rdd

    for x in rdd.collect():
        try:
            data = {   
                    'page': x['page'],
                    'post_id': x['post_id'],
                    'text': x['text'],
                    'timestamp': x['timestamp'],
                    'likes': int(x['likes']),
                    'comments': int(x['comments']),
                }
            es.index(index=normalize_index(x['page']), document=data)
        except:
            continue


def topic_modeling():
    global es, stop_words
    indices = es.cat.indices(format="json")
    all_data = []

    for index_info in indices:
        index_name = index_info['index']
        query = {
            "query": {
                "match_all": {}
            },
            "size": 10000
        }
        response = es.search(index=index_name, body=query)
        hits = response['hits']['hits']
        data = [hit['_source'] for hit in hits]
        all_data.extend(data)

    df = pd.DataFrame(all_data)
    
    likes_list = list(df['likes'])
    post_ids_list = list(df['post_id'])
    raw_data = list(df['text'])
    print(raw_data[0])
    print(type(raw_data[0]))
    print(clean_text(raw_data[0]))
    data = []
    for sample in raw_data:
        data.append(clean_text(sample))
    
    data_new = []
    for text in data:
        if len(text) != 0 and len(text) != 1:
            data_new.append(text)

    data_seg = []
    for text in data_new:
        try:
            tokens = rdrsegmenter.tokenize(text)[0]
            data_seg.append(' '.join(tokens))
        except:
            print(text)

    data_words = list(sent_to_words(data_seg))

    data_words_nostops = remove_stopwords(data_words, stop_words)

    data_words_bigrams = list(make_bigram(data_words_nostops))

    id2word = corpora.Dictionary(data_words_bigrams)
    texts = data_words_bigrams
    corpus = [id2word.doc2bow(text) for text in texts]

    lda_model = LdaModel(corpus=corpus,
                         id2word=id2word,
                         num_topics=10,
                         random_state=100,
                         update_every=1,
                         chunksize=100,
                         passes=5,
                         alpha='auto',
                         per_word_topics=True)
    
    lda_model.save("model_lda_100.model")

    df_topic_sents_keywords = format_topics_sentences(lda_model, corpus, post_ids_list)
    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Post_Id']

    dict = {}
    topics_list = df_dominant_topic.Keywords.unique()
    for topic in topics_list:
        dict.update({topic: []})
    for i, row in df_dominant_topic.iterrows():
        dict[row['Keywords']].append(row['Post_Id'])
    
    topics = lda_model.print_topics()
    print(topics)

    return dict


def get_posts_from_ids(post_ids):
    global es
    indices = es.cat.indices(format="json")
    post_texts = []

    for index_info in indices:
        index_name = index_info['index']
        query = {
            "query": {
                "terms": {
                    "post_id": post_ids
                }
            }
        }
        response = es.search(index=index_name, body=query)
        hits = response['hits']['hits']
        data = [hit['_source'] for hit in hits]
        post_texts.extend(data)

    return post_texts