# Generated by Django 4.1.3 on 2022-11-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Franchise', '0001_initial'),
        ('ERP', '0004_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobRole',
        ),
        migrations.AlterField(
            model_name='service',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Franchise.center'),
        ),
        migrations.DeleteModel(
            name='Center',
        ),
    ]
