from django.urls import path

from . import views


urlpatterns = [
    path('predict_topics/', views.predict_topics, name='predict_topics'),
    path('get_hot_topics/', views.get_hot_topics, name='get_hot_topics'),
    path('get_trending_posts/', views.get_trending_posts, name='get_trending_posts')
]