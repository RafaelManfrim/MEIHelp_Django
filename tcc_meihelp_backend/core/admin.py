from django.contrib import admin
from tcc_meihelp_backend.companies.models import Company
from tcc_meihelp_backend.transactions.models import Transaction

admin.site.register(Company)
admin.site.register(Transaction)
