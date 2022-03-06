from typing import OrderedDict
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.utils.translation import gettext_lazy as _
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','is_student','is_tech')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Home)
admin.site.register(Course)
admin.site.register(Category)
# admin.site.register(Teacher)
# admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(Video)
admin.site.register(BlogModel)
admin.site.register(blog_Category)
admin.site.register(Project_Category)
admin.site.register(User,UserAdmin)
# admin.site.register(absuser)