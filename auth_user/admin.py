# your django admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from auth_user.models import User

admin.site.register(User, UserAdmin)