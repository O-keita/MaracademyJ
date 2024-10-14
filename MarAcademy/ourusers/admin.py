from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define the fields to be used in displaying the CustomUser model in the admin interface.
    # These are the fields that are used to display the user list and user detail pages in the admin panel.
    list_display = ['username', 'email', 'is_staff', 'is_student', 'is_instructor']
    list_filter = ['is_staff', 'is_student', 'is_instructor']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Groups', {'fields': ('groups',)}),
        ('Custom Info', {'fields': ('is_student', 'is_instructor')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'profile_picture', 'password1', 'password2', 'is_student', 'is_instructor'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)