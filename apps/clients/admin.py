from django.contrib import admin
from apps.clients.models import Locations, Companies
from django.utils.translation import ugettext as _

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('company', 'linkToEmail', 'linkToTwitter', 'phone', 'industry', 'location')
	list_filter = ('industry', 'location', 'size',)
	search_fields = ['company']
	extra = 0

	def linkToEmail(self, Companies):
		return '<a href="mailto:' + Companies.email + '">' + Companies.email + '</a>'

	def linkToTwitter(self, Companies):
		if Companies.twitter != '@':
			return '<a href="http://twitter.com/' + Companies.twitter + '" target="_blank">' + Companies.twitter + '</a>'
		else:
			return ''
			
	linkToEmail.allow_tags = True
	linkToEmail.short_description = _('Email') 
	linkToTwitter.allow_tags = True
	linkToTwitter.short_description = 'Twitter' 

admin.site.register(Locations)
admin.site.register(Companies, CompaniesAdmin)