# Generated by Django 3.2.3 on 2021-05-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proHub', '0002_auto_20210529_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
