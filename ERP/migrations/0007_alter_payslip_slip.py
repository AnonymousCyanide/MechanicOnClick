# Generated by Django 4.1.3 on 2023-02-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0006_alter_payslip_slip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='slip',
            field=models.FileField(upload_to='media/payslips'),
        ),
    ]