# Generated by Django 4.0.3 on 2022-09-30 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_alter_training_created_at_alter_training_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 20, 15, 41, 482360), editable=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 20, 15, 41, 482375)),
        ),
    ]
