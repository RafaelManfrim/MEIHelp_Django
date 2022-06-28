from datetime import datetime

from django.db import models

from tcc_meihelp_backend.companies.models import Company


class DAS(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    mes = models.IntegerField('Mês')
    ano = models.IntegerField('Ano')
    vencimento = models.DateTimeField('Vencimento')
    total = models.DecimalField('Total', max_digits=10, decimal_places=2)
    status = models.CharField('Status', max_length=1)
    acolhimento = models.DateTimeField('Acolhimento')
    apuracao = models.DateTimeField('Apuração')
    pagamento = models.DateTimeField('Pagamento')
    url_das = models.CharField('URL DAS', max_length=255)
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'DAS'
        verbose_name_plural = 'DAS'
