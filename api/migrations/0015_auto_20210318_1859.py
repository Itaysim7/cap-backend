# Generated by Django 3.1.6 on 2021-03-18 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='office',
            name='start_date',
        ),
    ]
