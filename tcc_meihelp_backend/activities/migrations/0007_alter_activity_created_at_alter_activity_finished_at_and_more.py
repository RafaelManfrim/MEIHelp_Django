# Generated by Django 4.0.3 on 2022-10-17 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_alter_activity_created_at_alter_activity_finished_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307027), editable=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='finished_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307051), editable=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='forecast_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307012), verbose_name='Previsão de término'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307040)),
        ),
    ]
