from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CollectionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.collection"
    verbose_name = _("Collection")
