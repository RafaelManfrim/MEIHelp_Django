# Generated by Django 4.0.3 on 2022-09-30 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 19, 53, 42, 860028), editable=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 19, 53, 42, 860043)),
        ),
    ]
