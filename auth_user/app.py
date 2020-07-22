from django.apps import AppConfig


class AuthUserAppConfig(AppConfig):
    name = "auth_user"

    def ready(self):
        from auth_user import signals # pylint: disable=unused-variable
