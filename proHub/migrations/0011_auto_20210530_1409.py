# Generated by Django 3.2.3 on 2021-05-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proHub', '0010_alter_projects_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.FloatField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='creativity',
            field=models.FloatField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.FloatField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='mobile',
            field=models.FloatField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.FloatField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0.0, null=True),
        ),
    ]
