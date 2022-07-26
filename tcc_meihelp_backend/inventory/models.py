from django.db import models

from tcc_meihelp_backend.companies.models import Company


class BetterChoices(models.IntegerChoices):
    @classmethod
    def getValue(cls, label):
        try:
            labels = [lbl.lower() for lbl in cls.labels]
            pos = labels.index(label.lower())
            return cls.values[pos]
        except ValueError:
            return None

    @classmethod
    def getLabel(cls, value):
        try:
            pos = cls.values.index(value)
            return cls.labels[pos]
        except ValueError:
            return None


class ProductCategory(BetterChoices):
    Limpeza = 1, 'Limpeza'
    Saude = 2, 'Saúde'
    Alimentacao = 3, 'Alimentação'
    Moda = 4, 'Moda'
    Bebidas = 5, 'Bebidas'
    Tecnologia = 6, 'Tecnologia'
    Brinquedos = 7, 'Brinquedos'
    Outros = 8, 'Outros'


class Stock(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.PositiveSmallIntegerField('Categoria', choices=ProductCategory.choices)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)