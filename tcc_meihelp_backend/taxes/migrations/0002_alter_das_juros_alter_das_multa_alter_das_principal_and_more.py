# Generated by Django 4.0.3 on 2022-09-30 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='das',
            name='juros',
            field=models.CharField(max_length=7, verbose_name='Juros'),
        ),
        migrations.AlterField(
            model_name='das',
            name='multa',
            field=models.CharField(max_length=7, verbose_name='Multa'),
        ),
        migrations.AlterField(
            model_name='das',
            name='principal',
            field=models.CharField(max_length=7, verbose_name='Principal'),
        ),
        migrations.AlterField(
            model_name='das',
            name='total',
            field=models.CharField(max_length=7, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='das',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 19, 53, 42, 861074)),
        ),
    ]
