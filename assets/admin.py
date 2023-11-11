from django.contrib import admin
from assets.models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'image')


admin.site.register(Asset, AssetAdmin)
