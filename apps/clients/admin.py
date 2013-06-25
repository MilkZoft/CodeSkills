from django.contrib import admin
from apps.clients.models import Locations, Companies

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('company', 'email', 'linkToTwitter', 'phone', 'industry', 'location')
	list_filter = ('industry', 'location',)
	search_fields = ['company']
	extra = 0

	def linkToTwitter(self, Companies):
		return '<a href="http://twitter.com/' + Companies.twitter + '" target="_blank">' + Companies.twitter + '</a>'

	linkToTwitter.allow_tags = True
	
admin.site.register(Locations)
admin.site.register(Companies, CompaniesAdmin)