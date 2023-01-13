from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self) -> None:
        """ Starting the background scheduler """
        from scheduler import updater
        updater.start()
