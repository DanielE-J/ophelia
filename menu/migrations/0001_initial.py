# Generated by Django 5.2.1 on 2025-06-02 09:05

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('menu_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.menulist')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
