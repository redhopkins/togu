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
    
    url(r'admin_tools/', include('admin_tools.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^about/', views.page, name='about'),
    url(r'^services/', views.page, name='services'),
    url(r'^news/', views.news, name='news'),
    url(r'^admin/', include(admin.site.urls)),
) + static('/upload/', document_root='/home/ogo/repository/togu/togu/upload')

