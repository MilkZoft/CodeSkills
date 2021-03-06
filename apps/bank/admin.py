from django.contrib import admin
from apps.bank.models import Technologies, Categories, Developer_Level, Difficulty_Level, Profiles, Questions

class TechnologiesAdmin(admin.TabularInline):
	model = Technologies
	extra = 0

class ProfilesAdmin(admin.TabularInline):
	model = Profiles
	extra = 0

class CategoriesAdmin(admin.TabularInline):
	model = Categories
	extra = 0

class Developer_LevelAdmin(admin.TabularInline):
	model = Developer_Level
	extra = 0

class Difficulty_LevelAdmin(admin.TabularInline):
	model = Difficulty_Level
	extra = 0

class QuestionsAdmin(admin.ModelAdmin):
	list_display = ('id', 'tags', 'developer_level', 'difficulty_level', 'question_en', 'question_es',)
	list_filter = ('developer_level', 'difficulty_level', 'profiles', 'categories', 'technology',)
	search_fields = ['question_en']
	extra = 1

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Categories)
admin.site.register(Technologies)
admin.site.register(Developer_Level)
admin.site.register(Difficulty_Level)
admin.site.register(Profiles)