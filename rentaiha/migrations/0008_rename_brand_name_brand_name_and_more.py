# Generated by Django 4.1.7 on 2023-04-26 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaiha', '0007_alter_brand_id_alter_iha_brand_alter_iha_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='model_name',
            new_name='name',
        ),
    ]
