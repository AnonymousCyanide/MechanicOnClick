# Generated by Django 4.1.3 on 2023-02-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0015_centerservices_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
