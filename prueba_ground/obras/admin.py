from django.contrib import admin
from .models import Obras

# Register your models here.
class ObrasAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('Nombre','id',)

admin.site.register(Obras, ObrasAdmin)