from django.forms import ModelForm
from apps.bank.models import *

class BankForm(ModelForm):
	class Meta:
		model = Bank