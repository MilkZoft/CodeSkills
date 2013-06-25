from django.contrib import admin
from apps.clients.models import *

class CountriesAdmin(admin.TabularInline):
	model = Countries
	extra = 0

class CitiesAdmin(admin.TabularInline):
	model = Cities
	extra = 0

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('id', 'company',)
	search_fields = ['company']
	extra = 1

admin.site.register(Companies, CompaniesAdmin)
admin.site.register(CitiesAdmin)
admin.site.register(CountriesAdmin)