from django.conf.urls import patterns, include, url
from mysite import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^busca/', include('busca.urls')),
     url(r'^$', 'mysite.views.home', name='home'),
)
