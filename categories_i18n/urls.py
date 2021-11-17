from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category_list"),
    re_path(
        r"^(?P<slug>[-_\w]+)/$",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
