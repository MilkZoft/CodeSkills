from django.contrib import admin
from bank.models import Technologies, Categories, Developer_Level, Difficulty_Level, Profiles, Questions

class TechnologiesAdmin(admin.TabularInline):
	model = Technologies
	extra = 1

class ProfilesAdmin(admin.TabularInline):
	model = Profiles
	extra = 1

class CategoriesAdmin(admin.TabularInline):
	model = Categories
	extra = 1

class Developer_LevelAdmin(admin.TabularInline):
	model = Developer_Level
	extra = 1

class Difficulty_LevelAdmin(admin.TabularInline):
	model = Difficulty_Level
	extra = 1

class QuestionsAdmin(admin.ModelAdmin):
	list_display = ('id', 'developer_level', 'difficulty_level', 'question_en',)
	list_filter = ('developer_level', 'difficulty_level', 'technology',)
	search_fields = ['question_en'];

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Categories)
admin.site.register(Technologies)
admin.site.register(Developer_Level)
admin.site.register(Difficulty_Level)
admin.site.register(Profiles)