from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.bank.models import Questions, Technologies
from django.http import HttpResponseRedirect
from apps.bank import *

def index(request):
	questions = Questions.objects.all()

	return render_to_response(
		'bank_questions.html',
		RequestContext(request, locals())
	)

	if request.method == 'POST':
		bankForm = BankForm(request.POST)

		if bankForm.is_valid():
			bankForm.save()

			return HttpResponseRedirect('/')
	else:
		bankForm = BankForm()

def showQuestion(request, id):
	question = get_object_or_404(Questions, id = id)

	return render_to_response(
		'bank_question.html',
		RequestContext(request, locals())
	)