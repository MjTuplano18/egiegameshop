# Generated by Django 5.2 on 2025-04-17 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer_auth_provider_customer_firebase_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='auth_provider',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='firebase_uid',
        ),
    ]
