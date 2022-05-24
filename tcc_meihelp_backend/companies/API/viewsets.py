from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.companies.functions import validate_cnpj


class CNPJViewset(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    def validate(self, request):
        request_cnpj = request.data.get('cnpj')
        status_validacao = validate_cnpj(request_cnpj)
        return Response(status=status_validacao)


class CompanyViewset(viewsets.ModelViewSet):

    def list(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self):
        return Response({})

    def partial_update(self):
        return Response({})

    def destroy(self):
        return Response({})
