# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _

class Locations(models.Model):
	country = models.CharField('Country', max_length = 100)
	city    = models.CharField('City', max_length = 100)
	
	def __unicode__(self):
		return u'%s, %s' % (self.city, self.country)

	class Meta:
		verbose_name = _('Location')
		verbose_name_plural = _('Locations')	

class Companies(models.Model):
	location = models.ForeignKey(Locations)
	company  = models.CharField(_('Company2'), max_length = 150)
	contact  = models.TextField(null = True, blank = True, max_length = 100)
	address  = models.TextField(null = True, blank = True)
	email    = models.CharField('Email', null = True, blank = True, max_length = 120)
	skype 	 = models.CharField('Skype', null = True, blank = True, max_length = 60)
	website  = models.CharField('Website', default = 'http://', null = True, blank = True, max_length = 100)
	linkedin = models.CharField('Linkedin', null = True, blank = True, max_length = 60)
	twitter  = models.CharField('Twitter', default = '@', null = True, blank = True, max_length = 60)
	facebook = models.CharField('Facebook', null = True, blank = True, max_length = 60)
	phone    = models.CharField('Phone', null = True, blank = True, max_length = 15)
	mobile   = models.CharField('Mobile', null = True, blank = True, max_length = 15)
	industry = models.CharField('Industry', default = 'Software', null = True, blank = True, max_length = 100)

	def __unicode__(self):
		return self.company

	class Meta:
		ordering = ('company',)
		verbose_name = u'Company'
		verbose_name_plural = u'Companies'