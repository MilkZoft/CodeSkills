from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('apps.users.urls')),
   	url(r'^bank/', include('apps.bank.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^public/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'settings.MEDIA_ROOT'}),
    url(r'^public/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'settings.STATIC_ROOT'}),
)
