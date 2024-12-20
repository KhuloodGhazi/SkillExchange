# Generated by Django 5.1.4 on 2024-12-15 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_plan_alter_subscription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.plan'),
        ),
    ]
