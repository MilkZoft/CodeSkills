# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Companies(models.Model):
	country  = models.ForeignKey(Countries)
	city     = models.ForeignKey(Cities)
	company  = models.CharField('Company', max_length = 150)
	contact  = models.CharField('Contact', max_length = 100)
	address  = models.TextField()
	email    = models.CharField('Email', max_length = 120)
	phone    = models.CharField('Phone', max_length = 15)
	mobile   = models.CharField('Mobile', max_length = 15)
	industry = models.CharField('Industry', max_length = 100)

	def __unicode__(self):
		return self.company

	class Meta:
		ordering = ('company',)
		verbose_name = u'Company'
		verbose_name_plural = u'Companies'

class Countries(models.Model):
	country = models.CharField('Country', max_length = 50)
	
	def __unicode__(self):
		return self.country

	class Meta:
		ordering = ('country',)
		verbose_name = u'Country'
		verbose_name_plural = u'Countries'

class Cities(models.Model):
	city = models.CharField('City', max_length = 50)
	
	def __unicode__(self):
		return self.city

	class Meta:
		ordering = ('city',)
		verbose_name = u'City'
		verbose_name_plural = u'Cities'	