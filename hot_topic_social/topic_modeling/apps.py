from django.apps import AppConfig
from .ai_model import load


class TopicModelingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "topic_modeling"

    def ready(self):
        load()