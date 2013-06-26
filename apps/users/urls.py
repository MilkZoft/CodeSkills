from django.conf.urls.defaults import *

urlpatterns = patterns(
	'apps.users.views'
	url(r'^users/login/', 'login'),
)