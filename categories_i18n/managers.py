"""
The manager classes.
"""
import django
from django.db.models.query import QuerySet
from mptt.managers import TreeManager
from mptt.querysets import TreeQuerySet
from parler.managers import TranslatableManager, TranslatableQuerySet


class CategoryQuerySet(TranslatableQuerySet, TreeQuerySet):
    """
    The Queryset methods for the Category model.
    """

    def as_manager(cls):
        # Make sure the Django way of creating managers works.
        manager = CategoryManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager

    as_manager.queryset_only = True
    as_manager = classmethod(as_manager)


class CategoryManager(TreeManager, TranslatableManager):
    """
    Base manager class for the categories.
    """

    _queryset_class = CategoryQuerySet
