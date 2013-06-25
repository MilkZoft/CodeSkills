from django.contrib import admin
from apps.clients.models import Locations, Companies

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('company', 'linkToEmail', 'linkToTwitter', 'phone', 'industry', 'location')
	list_filter = ('industry', 'location',)
	search_fields = ['company']
	extra = 0

	def linkToEmail(self, Companies):
		return '<a href="mailto:' + Companies.email + '">' + Companies.email + '</a>'

	def linkToTwitter(self, Companies):
		return '<a href="http://twitter.com/' + Companies.twitter + '" target="_blank">' + Companies.twitter + '</a>'

	linkToEmail.allow_tags = True
	linkToTwitter.allow_tags = True

admin.site.register(Locations)
admin.site.register(Companies, CompaniesAdmin)