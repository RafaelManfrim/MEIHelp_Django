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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.company.corporate_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.PositiveSmallIntegerField('Categoria', choices=ProductCategory.choices)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + ProductCategory(self.category).label


class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} - {self.product.name} - {self.stock.name} / {self.stock.company.corporate_name}'


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone}'


class ProviderProducts(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} - {ProductCategory(self.product.category).label} / {self.provider.name}'
