from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile


User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Профиль пользователя'''
    list_display = ('user', 'first_name')
