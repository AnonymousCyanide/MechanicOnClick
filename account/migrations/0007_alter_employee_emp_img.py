# Generated by Django 4.1.3 on 2022-12-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_employee_emp_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_img',
            field=models.ImageField(default='static/empimg/AviDP.jpeg', upload_to='static/empimg'),
        ),
    ]