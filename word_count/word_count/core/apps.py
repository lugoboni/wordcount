from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "word_count.core"
    verbose_name = _("Core")

    def ready(self):
        try:
            import word_count.core.signals 
        except ImportError:
            pass
