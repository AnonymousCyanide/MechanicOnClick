# Generated by Django 4.1.3 on 2023-01-25 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_delete_carasouleelement_rename_content_booking_issue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
    ]
