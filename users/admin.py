from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_superuser', 'is_active', 'date_joined', 'last_login')


admin.site.register(CustomUser, CustomUserAdmin)
