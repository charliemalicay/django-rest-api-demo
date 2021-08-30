# Generated by Django 3.2.6 on 2021-08-30 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour_api', '0003_remove_package_highlighted_package'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='auth.user'),
            preserve_default=False,
        ),
    ]
