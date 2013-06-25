from django.contrib import admin
from apps.clients.models import Companies, Countries, Cities

class CountriesAdmin(admin.TabularInline):
	model = Countries
	extra = 0

class CitiesAdmin(admin.TabularInline):
	model = Cities
	extra = 0

class CompaniesAdmin(admin.ModelAdmin):
	model = Companies
	extra = 0

admin.site.register(CompaniesAdmin)
admin.site.register(CitiesAdmin)
admin.site.register(CountriesAdmin)