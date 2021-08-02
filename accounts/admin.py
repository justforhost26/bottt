from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


#
# admin.site.register(CustomUser, UserAdmin)
# UserAdmin.fieldsets += ("custom fields sets", {'fields': ('mobile_number', 'roll_no', 'year', 'department')}),


@admin.register(CustomUser)
class AdminUser(UserAdmin):
    list_display = ('mobile_number', 'roll_no', 'department',)
    # list_editable = ('mobile_number', 'roll_no', 'department',)
    ordering = ('email',)
    exclude = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
