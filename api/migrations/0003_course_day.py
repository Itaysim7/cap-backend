# Generated by Django 3.1.6 on 2021-02-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210212_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(choices=[(0, 'א'), (1, 'ב'), (2, 'ג'), (3, 'ד'), (4, 'ה'), (5, 'ו')], max_length=5, null=True),
        ),
    ]
