from django.db import models
from categories.models import Category, SubCategory


class Asset(models.Model):

    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='assets/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
