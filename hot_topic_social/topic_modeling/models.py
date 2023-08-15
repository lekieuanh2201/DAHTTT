from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.TextField()
    add_time = models.DateTimeField()
    post_ids_list = models.TextField()

    class Meta:
        managed = True

    def __str__(self):
        return self.name