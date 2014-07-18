from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from tools import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'togu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^contacts/', views.contacts, name='contacts'),
	url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^admin/', include(admin.site.urls)),
) + static('/upload/', document_root='/home/ogo/togu/upload')

