# Generated by Django 3.2 on 2023-06-06 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_auto_20230606_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamplatform',
            old_name='name',
            new_name='title',
        ),
    ]