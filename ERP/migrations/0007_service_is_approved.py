# Generated by Django 4.1.3 on 2023-01-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0006_remove_service_service_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]