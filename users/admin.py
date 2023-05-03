from django.contrib import admin

from users.models import MaralUser


# Register your models here.

@admin.register(MaralUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", 'is_active', 'email')