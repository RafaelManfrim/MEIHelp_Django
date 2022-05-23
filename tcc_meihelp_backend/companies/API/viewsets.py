from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.companies.functions import fetch_cnpj
from tcc_meihelp_backend.companies.models import CNPJ, Company


class CNPJViewset(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    def validate(self, request):
        request_cnpj = request.data.get('cnpj')

        try:
            cnpj = CNPJ.objects.get(cnpj=request_cnpj)

            if abs((cnpj.updated_at - datetime.now()).days) > 30:
                novos_dados, status_code = fetch_cnpj(request_cnpj)
                if status_code == status.HTTP_200_OK:
                    cnpj.updated_at = novos_dados['updated_at']
                    cnpj.is_mei = novos_dados['is_mei']
                    cnpj.save()

                    if cnpj.is_mei:
                        return Response(status=status.HTTP_200_OK)
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(status=status_code)

            else:
                if cnpj.is_mei:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        except CNPJ.DoesNotExist:
            novos_dados, status_code = fetch_cnpj(request_cnpj)
            if status_code == status.HTTP_200_OK:
                novo_cnpj = CNPJ.objects.create(**novos_dados)

                if novo_cnpj.is_mei:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status_code)


class CompanyViewset(viewsets.ModelViewSet):

    def list(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self):
        return Response({})

    def create(self):
        return Response({})

    def destroy(self):
        return Response({})
