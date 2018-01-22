from django.contrib.sites.models import Site
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from parler.fields import TranslatedField
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.utils.context import switch_language
from .managers import CategoryManager

try:
    from django.urls import reverse  # Django 1.10+
except ImportError:
    from django.core.urlresolvers import reverse


def _get_current_site():
    return Site.objects.get_current().pk


@python_2_unicode_compatible
class AbstractCategory(MPTTModel, TranslatableModel):
    """
    Base class for categories.
    """

    title = TranslatedField(any_language=True)
    slug = TranslatedField()  # Explicitly added, but not needed

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children', verbose_name=_('Parent'))
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, blank=True, null=True, default=_get_current_site)

    objects = CategoryManager()

    class Meta:
        abstract = True
        ordering = ('tree_id', 'lft')

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    def get_absolute_url(self):
        # Make sure i18n_patterns() generate the proper URL, when used.
        with switch_language(self):
            return reverse('category_detail', kwargs={'slug': self.slug})


class AbstractCategoryTranslation(TranslatedFieldsModel):
    """
    Base class for translated fields.
    """

    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=100, help_text=_("The slug is used in the URL of the page"))

    #: The ForeignKey to the shared model. Needs to be defined in the concrete class.
    master = None

    class Meta:
        abstract = True
        unique_together = (
            ('language_code', 'slug'),
        )
