from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CategoryAppConfig(AppConfig):
    """
    Application config for a better Django admin label.
    """
    name = 'categories_i18n'
    verbose_name = _("Categories")
