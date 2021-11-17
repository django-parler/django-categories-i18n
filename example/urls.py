from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path("admin/", include(admin.site.urls)),
    path("categories/", include("categories_i18n.urls")),
]
