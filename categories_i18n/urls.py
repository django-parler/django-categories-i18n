from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.CategoryListView.as_view(), name='category_list'),
    url('^(?P<slug>[-_\w]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
]
