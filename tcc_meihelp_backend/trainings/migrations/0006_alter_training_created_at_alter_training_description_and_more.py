# Generated by Django 4.0.3 on 2022-10-17 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0005_alter_training_created_at_alter_training_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307652), editable=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Descrição do vídeo'),
        ),
        migrations.AlterField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 15, 0, 10, 307667)),
        ),
    ]