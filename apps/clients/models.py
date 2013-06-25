# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Locations(models.Model):
	country = models.CharField('Country', max_length = 100)
	city    = models.CharField('City', max_length = 100)
	
	def __unicode__(self):
		return u'%s, %s' % (self.city, self.country)

	class Meta:
		verbose_name = u'Location'
		verbose_name_plural = u'Locations'	

class Companies(models.Model):
	location  = models.ForeignKey(Locations)
	company  = models.CharField('Company', max_length = 150)
	contact  = models.CharField('Contact', default = ' ', null = True, blank = True, max_length = 100)
	address  = models.TextField(null = True, default = ' ', blank = True)
	email    = models.CharField('Email', default = ' ', null = True, blank = True, max_length = 120)
	website  = models.CharField('website', default = ' ', null = True, blank = True, max_length = 100)
	twitter  = models.CharField('Twitter', default = ' ', null = True, blank = True, max_length = 60)
	facebook = models.CharField('Facebook', default = ' ', null = True, blank = True, max_length = 60)
	phone    = models.CharField('Phone', default = ' ', null = True, blank = True, max_length = 15)
	mobile   = models.CharField('Mobile', default = ' ', null = True, blank = True, max_length = 15)
	industry = models.CharField('Industry', default = ' ', null = True, blank = True, max_length = 100)

	def __unicode__(self):
		return self.company

	class Meta:
		ordering = ('company',)
		verbose_name = u'Company'
		verbose_name_plural = u'Companies'