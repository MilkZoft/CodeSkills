# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _

class Users(models.Model):
	username = models.CharField(_('Username'), max_length = 20)
	password = models.CharField(_('Password'), max_length = 40)
	email 	 = models.CharField(_('Email'), max_length = 100)
	
	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('Users')