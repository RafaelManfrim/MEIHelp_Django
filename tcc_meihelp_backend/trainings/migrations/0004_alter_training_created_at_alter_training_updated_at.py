# Generated by Django 4.0.3 on 2022-10-14 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_alter_training_created_at_alter_training_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 17, 32, 8, 860546), editable=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 17, 32, 8, 860560)),
        ),
    ]
