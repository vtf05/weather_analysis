# Generated by Django 5.1.3 on 2024-12-03 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('max_temp', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('min_temp', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('precipitation', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather_records', to='station.weatherstation')),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('station', 'date')},
            },
        ),
    ]