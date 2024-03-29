# Generated by Django 4.0.3 on 2022-09-30 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1028, verbose_name='URL do vídeo')),
                ('title', models.CharField(max_length=32, verbose_name='Nome do vídeo')),
                ('description', models.TextField(blank=True, max_length=128, null=True, verbose_name='Descrição do vídeo')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 9, 30, 19, 11, 29, 412425), editable=False)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 9, 30, 19, 11, 29, 412440))),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
    ]
