# Generated by Django 3.2.8 on 2021-10-19 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0003_auto_20211019_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('count', models.PositiveIntegerField(null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('source_received', models.CharField(max_length=50, null=True)),
                ('condition', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='assets/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.subcategory')),
            ],
        ),
    ]