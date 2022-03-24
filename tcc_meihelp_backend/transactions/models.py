from django.db import models


class Transaction(models.Model):
    class TransactionType(models.IntegerChoices):
        ENTRADA = 1, "Entrada"
        SAIDA = 2, "Saída"

    title = models.CharField('Título', max_length=32)
    description = models.TextField('Descrição', null=True, blank=True)
    amount = models.PositiveIntegerField('Valor')
    type = models.PositiveSmallIntegerField('Tipo', choices=TransactionType.choices)
    date = models.DateTimeField('Data')
    company_id = models.ForeignKey('companies.Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
