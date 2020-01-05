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

    def get_queryset(self):
        # Nasty: In some django-mptt 0.7 versions, TreeManager.get_querset() no longer calls super()
        # Hence, redefine get_queryset() here to have the logic from django-parler and django-mptt.
        return self._queryset_class(self.model, using=self._db).order_by(
            self.tree_id_attr, self.left_attr
        )
