from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrderItemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.orderItem"
    verbose_name = _("OrderItem")
