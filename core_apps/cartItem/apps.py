from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CartItemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.cartItem"
    verbose_name = _("CartItem")
