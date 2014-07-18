from django.conf.urls import patterns, url

from tools import views

urlpatterns = patterns(
    url(r'^index/', views.index, name='index'),
    url(r'^contacts/', views.contacts, name='contacts'),
)
