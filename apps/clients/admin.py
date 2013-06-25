from django.contrib import admin
from apps.clients.models import Locations, Companies

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('company', 'email', 'twitter', 'phone', 'industry')
	list_filter = ('industry',)
	search_fields = ['company']
	extra = 0

admin.site.register(Locations)
admin.site.register(Companies, CompaniesAdmin)