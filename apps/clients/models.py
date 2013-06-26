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
	company  = models.CharField(_('Company'), max_length = 150)
	contact  = models.TextField(_('Contact'), null = True, blank = True, max_length = 100)
	address  = models.TextField(_('Address'), null = True, blank = True)
	email    = models.CharField(_('Email'), null = True, blank = True, max_length = 120)
	skype 	 = models.CharField(_('Skype'), null = True, blank = True, max_length = 60)
	website  = models.CharField(_('Website'), default = 'http://', null = True, blank = True, max_length = 100)
	linkedin = models.CharField(_('Linkedin'), null = True, blank = True, max_length = 60)
	twitter  = models.CharField(_('Twitter'), default = '@', null = True, blank = True, max_length = 60)
	facebook = models.CharField(_('Facebook'), null = True, blank = True, max_length = 60)
	phone    = models.CharField(_('Phone'), null = True, blank = True, max_length = 30)
	mobile   = models.CharField(_('Mobile'), null = True, blank = True, max_length = 20)
	size     = models.CharField(_('Size'), default = 'Medium', null = True, blank = True, max_length = 20)
	industry = models.CharField(_('Industry'), default = 'Software', null = True, blank = True, max_length = 100)

	def __unicode__(self):
		return self.company

	class Meta:
		ordering = ('company',)
		verbose_name = u'Company'
		verbose_name_plural = u'Companies'