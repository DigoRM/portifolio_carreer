from django.apps import AppConfig


class PortifolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portifolio'

    def ready(self):
        # Register custom filters
        import portifolio.templatetags.custom_filters