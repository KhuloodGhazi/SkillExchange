# Generated by Django 5.1.3 on 2024-12-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_last_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
