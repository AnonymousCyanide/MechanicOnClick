# Generated by Django 4.1.3 on 2022-12-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_employee_center_employee_job_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_img',
            field=models.ImageField(default='img/team-1.jpg', upload_to='static/empimg'),
        ),
    ]
