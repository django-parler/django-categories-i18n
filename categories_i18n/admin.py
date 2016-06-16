from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.forms import MPTTAdminForm
from parler.admin import TranslatableAdmin
from .models import Category
from parler.forms import TranslatableModelForm


class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    """
    Form for categories, both MPTT + translatable.
    """
    pass


class CategoryAdmin(MPTTModelAdmin, TranslatableAdmin):
    """
    Admin page for categories.
    """
    list_display = ('title', 'slug')
    mptt_indent_field = 'title'  # be explicit for MPTT
    search_fields = ('translations__title', 'translations__slug')
    form = CategoryAdminForm

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'parent'),
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        # Needed for django-parler
        return {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
