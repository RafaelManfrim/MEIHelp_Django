from django.contrib import admin

from tcc_meihelp_backend.activities.models import Activity
from tcc_meihelp_backend.companies.models import Company, CNPJ
from tcc_meihelp_backend.inventory.models import Stock, Product, Provider, StockProduct, ProviderProducts
from tcc_meihelp_backend.taxes.models import DAS
from tcc_meihelp_backend.trainings.models import Training

admin.site.register(CNPJ)
admin.site.register(Company)
admin.site.register(Activity)
admin.site.register(Training)
admin.site.register(DAS)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(StockProduct)
admin.site.register(ProviderProducts)