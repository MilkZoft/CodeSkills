from django.conf.urls.default import *

urlspatterns = patterns(
	'apps.bank.views',
	url(r'^$', 'index', name = 'index'),
	url(r'^bank/questions/show/(?P<id>\d+)/$', 'showQuestion', name = 'question'),
)