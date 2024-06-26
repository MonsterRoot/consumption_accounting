# Generated by Django 4.0.6 on 2024-04-03 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Count number')),
                ('verify_date', models.DateField(verbose_name='Verify date')),
                ('two_tariff', models.BooleanField(default=False, verbose_name='Two-tariff')),
                ('units', models.CharField(max_length=20, verbose_name='Units')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('account_number', models.CharField(max_length=50, verbose_name='Account number')),
                ('meter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webui.meter', verbose_name='Meter')),
            ],
        ),
        migrations.CreateModel(
            name='Measuring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_t1', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Day')),
                ('value_t2', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Night')),
                ('meter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webui.meter', verbose_name='Meter')),
            ],
        ),
    ]
