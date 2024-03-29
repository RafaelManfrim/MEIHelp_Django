from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, cnpj, corporate_name, cep, email, phone, password, is_staff, is_superuser, **extra_fields):
        if not cnpj:
            raise ValueError('CNPJ é obrigatório')
        email = self.normalize_email(email)
        user = self.model(cnpj=cnpj, corporate_name=corporate_name, cep=cep, email=email, phone=phone,
                          password=password, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cnpj, corporate_name, cep, email, phone, password, **extra_fields):
        return self._create_user(cnpj, corporate_name, cep, email, phone, password, False, False, **extra_fields)

    def create_superuser(self, cnpj, corporate_name, cep, email, phone, password, **extra_fields):
        cnpj_banco = CNPJ.objects.get(cnpj=cnpj)
        user = self._create_user(cnpj_banco, corporate_name, cep, email, phone, password, True, True, **extra_fields)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CNPJ(models.Model):
    cnpj = models.CharField('CNPJ', max_length=14, validators=[MinLengthValidator(14)], unique=True, primary_key=True)
    updated_at = models.DateTimeField('Atualizado em')
    is_mei = models.BooleanField('É MEI')

    class Meta:
        verbose_name = 'CNPJ'
        verbose_name_plural = 'CNPJ'


class Company(AbstractBaseUser, PermissionsMixin):
    cnpj = models.OneToOneField(CNPJ, on_delete=models.CASCADE)
    email = models.EmailField('E-mail', max_length=50, unique=False)
    phone = models.CharField('Telefone', max_length=11)
    description = models.TextField('Descrição da MEI', null=True, blank=True)
    corporate_name = models.CharField('Razão social', max_length=100, unique=True)
    city = models.CharField('Cidade', max_length=80)
    cep = models.CharField('CEP', max_length=8, validators=[MinLengthValidator(8)], unique=False)
    uf = models.CharField('UF', max_length=2, validators=[MinLengthValidator(2)], unique=False)
    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(default=datetime.now())
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)

    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['corporate_name', 'email', 'phone', 'cep', 'city', 'uf']

    objects = UserManager()

    def __str__(self):
        return self.corporate_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
