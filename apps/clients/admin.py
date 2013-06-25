from django.contrib import admin
from apps.clients.models import Locations, Companies

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'email', 'website', 'twitter', 'facebook', 'phone', 'industry')
	list_filter = ('industry',)
	search_fields = ['company']
	extra = 0

admin.site.register(Locations)
admin.site.register(Companies, CompaniesAdmin)