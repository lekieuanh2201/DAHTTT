from datetime import datetime

from django.http import JsonResponse

from .models import Topic
from .ai_model import topic_modeling, get_posts_from_ids


# Create your views here.
def get_hot_topics(request):
    topics = Topic.objects.order_by('-add_time')
    topic_names = []
    if topics:
        for topic in topics:
            topic_names.append(topic.name)

    context = {
        'topic_names': topic_names,
    }

    return JsonResponse(context)


def get_trending_posts(request):
    topics = Topic.objects.order_by('-add_time')
    post_ids = []
    if topics:
        for topic in topics:
            post_ids.append(topic.post_ids_list.split('_')[0])

    post_texts = get_posts_from_ids(post_ids)
    context = {
        'post_texts': post_texts,
    }

    return JsonResponse(context)


def predict_topics(request):
    dict = topic_modeling()

    now = datetime.now()
    for key, items in dict.items():
        print(key)
        items = [str(item) for item in items]
        p = Topic(name=key, add_time = now, post_ids_list='_'.join(items))
        p.save()