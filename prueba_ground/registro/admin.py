from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('nombre', 'email', 'rut', 'direccion', 'pais', 'cp', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('nombre', 'password')}),
        ('Personal Info', {'fields': ('email', 'rut', 'direccion', 'pais', 'cp')}),
        ('Permissions', {'fields': ('admin', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre', 'password1', 'password2', 'email', 'rut', 'direccion', 'pais', 'cp', 'admin', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('nombre', 'email', 'rut', 'direccion', 'pais', 'cp')
    ordering = ('nombre',)

admin.site.register(CustomUser, CustomUserAdmin)
