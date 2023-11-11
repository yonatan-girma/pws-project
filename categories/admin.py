from django.contrib import admin
from categories.models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
