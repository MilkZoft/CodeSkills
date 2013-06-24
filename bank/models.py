# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Technologies(models.Model):
	technology = models.CharField(
		'Technology',
		max_length = 100,
		help_text = 'Write a technology'
	)

	common = models.BooleanField(default = 0)

	def __unicode__(self):
		return self.technology

	class Meta:
		ordering = ('common', 'technology',)
		verbose_name = u'Technology'
		verbose_name_plural = u'Technologies'

class Profiles(models.Model):
	profile = models.CharField(
		'Profile',
		max_length = 100,
		help_text = 'Write a profile'
	)

	def __unicode__(self):
		return self.profile

	class Meta:
		ordering = ('profile',)
		verbose_name = u'Profile'
		verbose_name_plural = u'Profiles'

class Categories(models.Model):
	category = models.CharField(
		'Category',
		max_length = 100,
		help_text = 'Write a category'
	)

	def __unicode__(self):
		return self.category

	class Meta:
		ordering = ('category',)
		verbose_name = u'Category'
		verbose_name_plural = u'Categories'

class Developer_Level(models.Model):
	developer_level = models.CharField(
		'Developer Level',
		max_length = 100,
		help_text = 'Write a developer level: Junior, Mid, Senior, Expert'
	)

	def __unicode__(self):
		return self.developer_level

	class Meta:
		verbose_name = u'Developer Level'
		verbose_name_plural = u'Developer Levels'

class Difficulty_Level(models.Model):
	difficulty_level = models.CharField(
		'Difficulty Level',
		max_length = 100,
		help_text = 'Write a difficulty level: Easy, Medium, Hard, Expert'
	)

	def __unicode__(self):
		return self.difficulty_level

	class Meta:
		verbose_name = u'Difficulty Level'
		verbose_name_plural = u'Difficulty Levels'

class Questions(models.Model):
	categories = models.ManyToManyField(Categories)
	profiles = models.ManyToManyField(Profiles)
	technology = models.ManyToManyField(Technologies)
	developer_level = models.ForeignKey(Developer_Level)
	difficulty_level = models.ForeignKey(Difficulty_Level)

	question_en = models.CharField(
		'English Question',
		max_length = 200,
		help_text = 'Write the English question'
	)

	question_es = models.CharField(
		'Spanish Question',
		max_length = 200,
		help_text = 'Write the Spanish question'
	)

	answer_en = models.TextField()

	answer_es = models.TextField()

	tags = models.CharField(
		'Tags',
		max_length = 150
	)

	times_used = models.PositiveSmallIntegerField(default = 0)

	creation_date = models.DateField("Creation Date", default = datetime.today)

	status = models.CharField(
		'Status',
		max_length = 20,
		default = 'Active'
	)

	def __unicode__(self):
		return self.question_en

	class Meta:
		ordering = ('id', 'question_en',)
		verbose_name = u'Question'
		verbose_name_plural = u'Questions'