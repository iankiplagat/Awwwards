# Generated by Django 3.2.3 on 2021-05-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proHub', '0009_alter_projects_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(),
        ),
    ]
