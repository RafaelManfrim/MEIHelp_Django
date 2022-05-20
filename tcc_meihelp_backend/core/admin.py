from django.contrib import admin
from tcc_meihelp_backend.companies.models import Company, CNPJ

admin.site.register(CNPJ)
admin.site.register(Company)
