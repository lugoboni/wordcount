from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "word_count.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import word_count.users.signals  # noqa F401
        except ImportError:
            pass
