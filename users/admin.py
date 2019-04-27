from django.contrib import admin

from users.models import Client, Clinic

# Register your models here.

admin.site.register(Client)
admin.site.register(Clinic)
