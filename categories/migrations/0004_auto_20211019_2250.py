# Generated by Django 3.2.8 on 2021-10-19 22:50

from django.db import migrations
from django.core.files import File
from pws.categories import CATEGORIES


def preload_categories_and_subcategories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    SubCategory = apps.get_model('categories', 'SubCategory')
    for category in CATEGORIES:
        category_obj = Category.objects.create(title=category['title'], image=File(open(category['image_url'], 'rb')))
        SubCategory.objects.bulk_create(SubCategory(title=sub_category['title'],
                                                    image=File(open(category['image_url'], 'rb')),
                                                    category=category_obj) for sub_category in category['sub_categories'])


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20211019_2106'),
    ]

    operations = [
        migrations.RunPython(preload_categories_and_subcategories),
    ]
