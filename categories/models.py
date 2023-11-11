from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='categories/', null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='subcategories/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.title
