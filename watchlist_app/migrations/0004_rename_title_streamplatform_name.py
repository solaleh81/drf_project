# Generated by Django 3.2 on 2023-06-06 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_rename_name_streamplatform_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamplatform',
            old_name='title',
            new_name='name',
        ),
    ]