# Generated by Django 4.0.6 on 2022-09-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_images_product_main_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
