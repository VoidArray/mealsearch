from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<search>\w+)/$', views.search_result, name='search_result'),
]