from django.contrib import admin
from apps.clients.models import Countries, Cities, Companies

class CountriesAdmin(admin.TabularInline):
	model = Countries
	extra = 0

admin.site.register(CountriesAdmin)