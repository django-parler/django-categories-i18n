from django.urls import include, path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', include(admin.site.urls)),
    path('categories/', include("categories_i18n.urls")),
]
