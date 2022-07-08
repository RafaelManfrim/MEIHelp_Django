import requests

from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from tcc_meihelp_backend.companies.API.serializers import CompanyTokenObtainPairSerializer, CompaniesSerializer
from tcc_meihelp_backend.companies.functions import validate_cnpj
from tcc_meihelp_backend.companies.models import Company, CNPJ


class CNPJViewset(viewsets.ViewSet):
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def validate(self, request):
        request_cnpj = request.data.get('cnpj')
        status_validacao = validate_cnpj(request_cnpj)
        return Response(status=status_validacao)


class CompanyViewset(viewsets.ViewSet):
    @action(methods=['GET'], detail=False)
    def all(self, request):
        user = request.user
        companies = Company.objects.filter(description__isnull=False).filter(~Q(id=user.id))
        serializer = CompaniesSerializer(companies, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        request_cnpj = request.data.get('cnpj')

        dados = {
            'phone': request.data.get('phone'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }

        try:
            response = requests.get('https://receitaws.com.br/v1/cnpj/' + request_cnpj)

            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'ERROR':
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                dados['cep'] = data['cep'].replace(".", "").replace("-", "")
                dados['uf'] = data['uf']
                dados['city'] = data['municipio']
                dados['corporate_name'] = data['nome']

            if response.status_code == 429 or response.status_code == 504:
                return Response(status=response.status_code)

        except requests.exceptions.RequestException:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            cnpj = CNPJ.objects.get(cnpj=request_cnpj)
            dados['cnpj'] = cnpj
        except CNPJ.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Company.objects.create_user(**dados)

        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False)
    def full_data(self, request):
        company = request.user

        data = {
            'corporate_name': company.corporate_name,
            'description': company.description,
            'cep': company.cep,
            'phone': company.phone,
            'email': company.email,
        }

        return Response(data)

    @action(methods=['PATCH'], detail=False)
    def update_data(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        description = request.data.get('description')
        cep = request.data.get('cep')

        company = request.user

        company.email = email
        company.phone = phone
        company.description = description
        company.cep = cep
        company.save()

        return Response()

    @action(methods=['DELETE'], detail=False)
    def delete(self, request):
        request.user.delete()

        return Response()


class CompanyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CompanyTokenObtainPairSerializer
