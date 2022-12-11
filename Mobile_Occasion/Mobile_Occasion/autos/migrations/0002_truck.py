# Generated by Django 4.1.4 on 2022-12-11 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('fuel', models.CharField(choices=[('Diesel', 'Diesel'), ('Gasoline', 'Gasoline')], max_length=8)),
                ('category', models.CharField(blank=True, choices=[('Box', 'Box'), ('Car carrier', 'Car carrier'), ('Dumper truck', 'Dumper truck'), ('Food Carrier', 'Food Carrier'), ('Grain Truck', 'Grain Truck'), ('Mining Truck', 'Mining Truck'), ('Hydraulic Platform', 'Hydraulic Platform'), ('Over truck over 7.5 t', 'Over truck over 7.5 t')], max_length=21, null=True)),
                ('first_reg_date', models.DateField()),
                ('price', models.CharField(max_length=15)),
                ('kilometers', models.CharField(max_length=15)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=9)),
                ('photo1', models.URLField()),
                ('photo2', models.URLField(blank=True, null=True)),
                ('photo3', models.URLField(blank=True, null=True)),
                ('photo4', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
