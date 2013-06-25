from django.contrib import admin
from apps.clients.models import Companies, Countries, Cities

class CountriesAdmin(admin.TabularInline):
	model = Countries
	extra = 0

class CitiesAdmin(admin.TabularInline):
	model = Cities
	extra = 0

class CompaniesAdmin(admin.ModelAdmin):
	list_display = ('id', 'company')
	search_fields = ['company']
	extra = 1

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Categories)
admin.site.register(Technologies)
admin.site.register(Developer_Level)
admin.site.register(Difficulty_Level)
admin.site.register(Profiles)