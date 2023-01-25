# Generated by Django 4.1.3 on 2023-01-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0009_alter_service_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='progress',
            field=models.CharField(choices=[('WAITING', 'Waiting'), ('DOING', 'Doing')], default='WAITING', max_length=20),
        ),
    ]
