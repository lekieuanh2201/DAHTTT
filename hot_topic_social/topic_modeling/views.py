import re

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from vncorenlp import VnCoreNLP
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel
# from elastic_search import Elasticsearch

# from .models import Topic
from .ai_model import topic_modeling, get_posts_from_ids

# Create your views here.
# def get_posts_on_topic(request, topic_name):
#     topic_name = clean_text(topic_name)
#     topic_posts = models.Topic_post.objects.filter(topic__name=topic_name)
#     posts = []
#     if topic_posts:
#         for topic_post in topic_posts:
#             post = models.Post.objects.get(post_id=topic_post['post'])
#             if post:
#                 posts.append(post['content'])
    
#     context = {
#         'posts': posts,
#     }

#     return JsonResponse(context)


# def get_hot_topics(request):
#     topics = Topic.objects.order_by('-add_time')
#     topic_names = []
#     if topics:
#         for topic in topics:
#             topic_names.append(topic['name'])

#     context = {
#         'topic_names': topic_names,
#     }

#     return JsonResponse(context)


# def get_trending_posts(request):
#     topics = Topic.objects.order_by('-add_time')
#     post_ids = []
#     if topics:
#         for topic in topics:
#             post_ids.append(topic['post_ids_list'].split('_')[0])

#     post_texts = get_posts_from_ids(post_ids)
#     context = {
#         'post_texts': post_texts,
#     }

#     return JsonResponse(context)


# def topic_modeling(request, category, es):
#     index_name = category
#     search_query = {
#     "query": {
#         "match_all": {}  # Retrieve all documents
#             }}
    
#     response = es.search(index=index_name, body=search_query, size=1000)  # Adjust the size as needed
#     hits = response['hits']['hits']

#     data = [hit['_source'] for hit in hits]
#     df = pd.DataFrame(data)

#     # df = pd.read_csv(csv_file, header=None)
#     raw_data = df[1]

#     data = [clean_text(str(sample)) for sample in raw_data]
#     data_new = []
#     for text in data:
#         if len(text) != 0 and len(text) != 1:
#             data_new.append(text)

#     rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')

#     data_seg = []
#     for text in data_new:
#         try:
#             tokens = rdrsegmenter.tokenize(text)[0]
#             data_seg.append(' '.join(tokens))
#         except:
#             print(text)

#     data_words = list(sent_to_words(data_seg))

#     stop_words = []
#     with open('vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             stop_words.append(line[:-1])

#     data_words_nostops = remove_stopwords(data_words, stop_words)

#     data_words_bigrams = list(make_bigram(data_words_nostops))

#     id2word = corpora.Dictionary(data_words_bigrams)
#     texts = data_words_bigrams
#     corpus = [id2word.doc2bow(text) for text in texts]

#     lda_model = LdaModel(corpus=corpus,
#                          id2word=id2word,
#                          num_topics=10,
#                          random_state=100,
#                          update_every=1,
#                          chunksize=100,
#                          passes=5,
#                          alpha='auto',
#                          per_word_topics=True)
    
#     lda_model.save("model_lda_100.model")

#     topics = lda_model.print_topics()

#     context = {
#         'topics': topics,
#     }

#     return JsonResponse(context)


def predict_topics(request):
    topic_modeling()

    context = {}

    return JsonResponse(context)