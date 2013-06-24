from django.forms import ModelForm
from bank.models import *

class BankForm(ModelForm):
	model = Bank