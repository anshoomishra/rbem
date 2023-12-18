from django.contrib import admin
from .models import AssemblyUser,AssemblyUserGroup
# Register your models here.

admin.site.register(AssemblyUser)
admin.site.register(AssemblyUserGroup)