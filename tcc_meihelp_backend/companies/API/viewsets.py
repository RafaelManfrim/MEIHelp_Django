import requests

from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.companies.functions import validate_cnpj
from tcc_meihelp_backend.companies.models import Company, CNPJ, UserManager


class CNPJViewset(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    def validate(self, request):
        request_cnpj = request.data.get('cnpj')
        status_validacao = validate_cnpj(request_cnpj)
        return Response(status=status_validacao)


class CompanyViewset(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
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

                dados['cep'] = data['cep']
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

    def partial_update(self, request, *args, **kwargs):
        return Response({})

    def destroy(self, request, *args, **kwargs):
        return Response({})
