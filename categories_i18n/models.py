from django.db import models
from django.utils.translation import ugettext_lazy as _
from categories_i18n.abstract_models import AbstractCategory, AbstractCategoryTranslation


class Category(AbstractCategory):
    """
    The category model.
    """
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('tree_id', 'lft')


class CategoryTranslation(AbstractCategoryTranslation):
    """
    The translated fields of the category.
    By using this model instead of the ``parler.models.TranslatedFields(..)`` construct,
    the translatable fields can be defined in an abstract model.
    """
    master = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='translations')

    class Meta:
        verbose_name = _("Category Translation")
        verbose_name_plural = _("Category Translations")
