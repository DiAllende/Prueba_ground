from django.contrib import admin
from .models import UsersRegistro

# Register your models here.
class UsersAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(UsersRegistro, UsersAdmin)