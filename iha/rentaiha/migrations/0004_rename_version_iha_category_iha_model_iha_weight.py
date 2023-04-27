# Generated by Django 4.1.7 on 2023-04-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentaiha', '0003_iha_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iha',
            old_name='version',
            new_name='category',
        ),
        migrations.AddField(
            model_name='iha',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iha',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
