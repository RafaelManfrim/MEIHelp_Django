# Generated by Django 4.0.3 on 2022-03-24 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('amount', models.PositiveIntegerField(verbose_name='Valor')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Entrada'), (2, 'Saída')], verbose_name='Tipo')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]