from django.conf.urls.defaults import *

urlpatterns = patterns(
	'apps.users.views',
	url(r'^$', 'index', name = 'index'),
	url(r'^bank/questions/show/(?P<id>\d+)/$', 'showQuestion', name = 'question'),
)