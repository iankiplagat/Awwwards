# Generated by Django 3.2.3 on 2021-05-29 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proHub', '0004_alter_projects_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='country',
        ),
    ]