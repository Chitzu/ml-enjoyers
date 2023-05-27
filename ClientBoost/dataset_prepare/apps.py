from django.apps import AppConfig


class DatasetPrepareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataset_prepare'

    def ready(self):
        from . import serializers