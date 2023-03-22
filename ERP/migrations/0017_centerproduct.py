# Generated by Django 4.1.3 on 2023-03-12 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Franchise', '0001_initial'),
        ('ERP', '0016_estimate_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default='Diam dolor diam ipsum sit amet diam et eos erat ipsum', max_length=400)),
                ('price', models.IntegerField(default=500)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('tax', models.FloatField(default=5)),
                ('stock', models.IntegerField(default=0)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Franchise.center')),
            ],
        ),
    ]