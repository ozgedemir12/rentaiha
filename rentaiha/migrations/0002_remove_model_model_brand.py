# Generated by Django 4.1.7 on 2023-04-25 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaiha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='model_brand',
        ),
    ]