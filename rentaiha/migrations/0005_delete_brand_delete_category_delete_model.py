# Generated by Django 4.1.7 on 2023-04-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaiha', '0004_brand_category_model'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
    ]