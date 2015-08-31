from django.views.generic import DetailView, ListView
from parler.views import TranslatableSlugMixin
from .models import Category


class CategoryListView(ListView):
    """
    Category list view.
    """
    model = Category


class CategoryDetailView(TranslatableSlugMixin, DetailView):
    """
    Category detail view
    """
    model = Category
