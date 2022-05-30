from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tcc_meihelp_backend.companies.functions import validate_cnpj
from tcc_meihelp_backend.companies.models import Company


class CompaniesSerializer(serializers.Serializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CompanyTokenObtainPairSerializer, self).validate(attrs)
        status_validacao = validate_cnpj(self.user.cnpj.cnpj)

        data.update({'user': {
            'corporate_name': self.user.corporate_name,
            'description': self.user.description
        }})
        data.update({'status': status_validacao})

        return data
