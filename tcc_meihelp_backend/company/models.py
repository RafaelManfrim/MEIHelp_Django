from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, cnpj, corporate_name, fantasy_name, email, phone, password, is_staff, is_superuser, **extra_fields):
        if not cnpj:
            raise ValueError('CNPJ é obrigatório')
        email = self.normalize_email(email)
        user = self.model(cnpj=cnpj, corporate_name=corporate_name, fantasy_name=fantasy_name, email=email, phone=phone,
                          password=password, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cnpj, corporate_name, fantasy_name, email, phone, password, **extra_fields):
        return self._create_user(cnpj, corporate_name, fantasy_name, email, phone, password, False, False, **extra_fields)

    def create_superuser(self, cnpj, corporate_name, fantasy_name, email, phone, password, **extra_fields):
        user = self._create_user(cnpj, corporate_name, fantasy_name, email, phone, password, True, True, **extra_fields)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Company(AbstractBaseUser, PermissionsMixin):
    cnpj = models.CharField('CNPJ', max_length=16, unique=True)
    corporate_name = models.CharField('Razão social', max_length=128)
    fantasy_name = models.CharField('Nome fantasia', max_length=64)
    email = models.EmailField('E-mail', max_length=64, unique=False)
    phone = models.CharField('Telefone', max_length=32)
    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(default=datetime.now())
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)

    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['corporate_name', 'fantasy_name', 'email', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.corporate_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
