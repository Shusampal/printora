from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        """Initialize admin customization when apps are ready"""
        from printora.admin_customization import customize_admin_site
        customize_admin_site()
