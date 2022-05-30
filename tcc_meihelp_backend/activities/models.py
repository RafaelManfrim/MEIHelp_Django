from datetime import datetime

from django.db import models

from tcc_meihelp_backend.companies.models import Company


class Activity(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=32)
    description = models.TextField('Descrição do compromisso', null=True, blank=True)
    finished = models.BooleanField('Finalizado')
    forecast_date = models.DateField('Previsão de término', default=datetime.now())
    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(default=datetime.now())
    finished_at = models.DateTimeField(default=datetime.now(), editable=False)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
