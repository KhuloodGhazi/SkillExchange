# Generated by Django 5.1.4 on 2024-12-17 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_subscription_plan_remove_subscription_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimony',
            old_name='comment',
            new_name='testimony_comment',
        ),
    ]