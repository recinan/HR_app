from django.apps import AppConfig


class EvaulationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evaulation'

    def ready(self):
        import notification.signals
