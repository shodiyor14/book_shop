# Generated by Django 4.1.5 on 2023-01-24 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='LaptopCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='LaptopColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='LaptopTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='LaptopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('graphics_card', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('Built_in_memory', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('Country_of_manufacture', models.CharField(max_length=10)),
                ('Display_screen_type', models.CharField(max_length=19)),
                ('Screen_dioganal', models.CharField(max_length=19)),
                ('Screen_Resolution', models.CharField(max_length=30)),
                ('processor', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='laptop', to='laptop.laptopbrandmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='laptop', to='laptop.laptopcategorymodel')),
                ('color', models.ManyToManyField(related_name='laptop', to='laptop.laptopcolormodel')),
                ('tag', models.ManyToManyField(related_name='laptop', to='laptop.laptoptagmodel')),
            ],
            options={
                'verbose_name': 'laptop',
                'verbose_name_plural': 'laptops',
            },
        ),
    ]
