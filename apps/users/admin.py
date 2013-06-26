from django.contrib import admin
from apps.users.models import Users
from django.utils.translation import ugettext as _

class UsersAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'email')
	search_fields = ['username']
	extra = 0

admin.site.register(Users, UsersAdmin)