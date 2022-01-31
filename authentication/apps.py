from django.apps import AppConfig

from django.core.signals import request_finished


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    # to connect the signals
    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
