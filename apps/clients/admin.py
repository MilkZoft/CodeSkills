from django.contrib import admin
from apps.clients.models import Countries, Cities, Companies

admin.site.register(Countries)
admin.site.register(Cities)
admin.site.register(Companies)