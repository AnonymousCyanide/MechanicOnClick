# Generated by Django 4.1.3 on 2022-12-17 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_employee_emp_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='facbook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='insta_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='on_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_img',
            field=models.ImageField(default='media/empimg/AviDP.jpeg', upload_to='static/empimg'),
        ),
    ]
