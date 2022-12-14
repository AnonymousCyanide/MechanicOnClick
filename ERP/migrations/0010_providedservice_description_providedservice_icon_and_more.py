# Generated by Django 4.1.3 on 2022-12-17 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0009_providedservice_price_alter_service_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='providedservice',
            name='description',
            field=models.CharField(default='Diam dolor diam ipsum sit amet diam et eos erat ipsum', max_length=400),
        ),
        migrations.AddField(
            model_name='providedservice',
            name='icon',
            field=models.CharField(default='fa fa-certificate fa-3x text-primary flex-shrink-0', max_length=50),
        ),
        migrations.AddField(
            model_name='providedservice',
            name='on_display',
            field=models.BooleanField(default=False),
        ),
    ]
