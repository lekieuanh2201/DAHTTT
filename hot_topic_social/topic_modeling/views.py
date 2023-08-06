import re

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from vncorenlp import VnCoreNLP
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel

from topic_modeling import models

# Create your views here.
def clean_text(text):
    text = re.sub(r'[^\w\s]', r'', text)
    text = re.sub(r'\n', r' ', text)
    text = re.sub(r' +', r' ', text)
    text = text.strip().lower()
    return text

def get_posts_on_topic(request, topic_name):
    topic_name = clean_text(topic_name)
    topic_posts = models.Topic_post.objects.filter(topic__name=topic_name)
    posts = []
    if topic_posts:
        for topic_post in topic_posts:
            post = models.Post.objects.get(post_id=topic_post['post'])
            if post:
                posts.append(post['content'])
    
    context = {
        'posts': posts,
    }

    return JsonResponse(context)


def get_hot_topics(request):
    topics = models.Topic.objects.order_by('-add_time')
    topic_names = []
    if topics:
        for topic in topics:
            topic_names.append(topic['name'])

    context = {
        'topic_names': topic_names,
    }

    return JsonResponse(context)


def get_trending_posts(request):
    posts = models.Post.objects.order_by('-num_like')
    post_contents = []
    if posts:
        for post in posts:
            post_contents.append(post['content'])
    
    context = {
        'post_contents': post_contents,
    }

    return JsonResponse(context)


def sent_to_words(sentences):
    for sentence in sentences:
        yield(sentence.split(' '))

def remove_stopwords(texts, stop_words):
    return [[word for word in simple_preprocess(doc) if word not in stop_words] for doc in texts]

def make_bigram(texts):
    for text in texts:
        new_text = text
        for i in range(len(text)-1):
            bigram = text[i] + ' ' + text[i+1]
            new_text.append(bigram)
        yield(new_text)

def topic_modeling(request, csv_file):
    df = pd.read_csv(csv_file, header=None)
    raw_data = df[1]

    data = [clean_text(str(sample)) for sample in raw_data]
    data_new = []
    for text in data:
        if len(text) != 0 and len(text) != 1:
            data_new.append(text)

    rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')

    data_seg = []
    for text in data_new:
        try:
            tokens = rdrsegmenter.tokenize(text)[0]
            data_seg.append(' '.join(tokens))
        except:
            print(text)

    data_words = list(sent_to_words(data_seg))

    stop_words = []
    with open('vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line[:-1])

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

    topics = lda_model.print_topics()

    context = {
        'topics': topics,
    }

    return JsonResponse(context)