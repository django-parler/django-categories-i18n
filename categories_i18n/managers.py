"""
The manager classes.
"""
import django
from django.db.models.query import QuerySet
from mptt.managers import TreeManager
from parler.managers import TranslatableManager, TranslatableQuerySet

try:
    # mptt 0.7 has queryset methods too
    from mptt.querysets import TreeQuerySet
except ImportError:
    # provide compatibility with older mptt versions by adding a stub.
    class TreeQuerySet(QuerySet):
        pass


class CategoryQuerySet(TranslatableQuerySet, TreeQuerySet):
    """
    The Queryset methods for the Category model.
    """
    def as_manager(cls):
        # Make sure the Django 1.7 way of creating managers works.
        manager = CategoryManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager
    as_manager.queryset_only = True
    as_manager = classmethod(as_manager)


class CategoryManager(TreeManager, TranslatableManager):
    """
    Base manager class for the categories.
    """
    # This attribute is now a standard property in Django 1.7:
    _queryset_class = CategoryQuerySet

    def get_queryset(self):
        return self._queryset_class(self.model, using=self._db).order_by(self.tree_id_attr, self.left_attr)

    # For Django 1.5
    if django.VERSION < (1, 7):
        get_query_set = get_queryset
