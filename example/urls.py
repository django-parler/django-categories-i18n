from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^categories/", include("categories_i18n.urls")),
]
