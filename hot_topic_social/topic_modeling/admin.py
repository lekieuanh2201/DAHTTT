from django.contrib import admin

from .models import Post, Topic, Topic_post

# Register your models here.
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Topic_post)