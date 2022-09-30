from datetime import datetime

from django.db import models

from tcc_meihelp_backend.companies.models import Company


class DAS(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    mes = models.IntegerField('Mês')
    ano = models.IntegerField('Ano')
    apurado = models.CharField('Apuração', max_length=3)
    situacao = models.CharField('Status', max_length=32)
    principal = models.CharField('Principal', max_length=7)
    multa = models.CharField('Multa', max_length=7)
    juros = models.CharField('Juros', max_length=7)
    total = models.CharField('Total', max_length=7)
    data_vencimento = models.DateField('Vencimento', null=True, blank=True)
    data_acolhimento = models.DateField('Acolhimento', null=True, blank=True)
    url_das = models.CharField('URL DAS', max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'DAS'
        verbose_name_plural = 'DAS'
