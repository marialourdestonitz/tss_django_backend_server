from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReviewConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.review"
    verbose_name = _("Review")
