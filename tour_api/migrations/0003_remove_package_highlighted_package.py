# Generated by Django 3.2.6 on 2021-08-30 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_api', '0002_auto_20210829_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='highlighted_package',
        ),
    ]
