# Generated by Django 4.1.3 on 2023-02-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0002_payslip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='slip',
            field=models.FileField(blank=True, null=True, upload_to='media/updateimg'),
        ),
    ]