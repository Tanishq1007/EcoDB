# Generated by Django 5.1.1 on 2024-10-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0004_alter_brand_logo_alter_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
