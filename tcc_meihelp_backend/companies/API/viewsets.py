import requests
from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.companies.models import CNPJ


class CNPJViewset(viewsets.ViewSet):
    @action(methods=['POST'], detail=False)
    def validate(self, request):
        request_cnpj = request.data.get('cnpj')

        try:
            # Verificar se o cnpj já existe no banco
            cnpj = CNPJ.objects.get(cnpj=request_cnpj)
            # return Response({'cnpj': cnpj})
            # Verificar se updated_at foi atualizado a mais de 30 dias
            if abs((cnpj.updated_at - datetime.now()).days) > 30:
                print('Entrou aqui')
                # Atualizar dados referentes ao CNPJ
                # Validar se é MEI
                # Salvar no banco
            else:
                print('Entrou aqui 2')
                # Se não, utilizar os dados do banco
        except CNPJ.DoesNotExist:
            response = requests.get('https://receitaws.com.br/v1/cnpj/' + request_cnpj)
            data = response.json()

            infos = {
                'cep': data['cep'],
                'corporate_name': data['nome'],
                'cnpj': data['cnpj']
            }

            if data['natureza_juridica'].startswith('213-5'):
                infos['isMEI'] = True
            return Response(data)
            # Buscar dados referentes ao CNPJ
            # Validar se é MEI
            # Salvar no banco

        # Se for uma MEI Válida, retornar os dados para o front, se não, retornar um erro avisando

        # return Response({'cnpj': response})
