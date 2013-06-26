from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.users.models import Users
from django.http import HttpResponseRedirect

def login(request):
	return render_to_response(
		'users_login.html',
		RequestContext(request, locals())
	)