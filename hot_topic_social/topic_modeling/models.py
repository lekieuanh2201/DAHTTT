from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    content = models.TextField()
    num_like = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = True

    def __str__(self):
        return self.content
    

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.TextField()
    add_time = models.DateTimeField()

    class Meta:
        managed = True

    def __str__(self):
        return self.name
    

class Topic_post(models.Model):
    topic = models.OneToOneField(Topic, models.DO_NOTHING, primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('topic', 'post'),)

    def get_topic_id(self):
        return self.topic
    
    def get_post_id(self):
        return self.post
    
    def __str__(self):
        return self.topic + ' ' + self.post