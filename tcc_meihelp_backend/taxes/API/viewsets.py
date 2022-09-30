from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.taxes.API.serializers import DasSerializer
from tcc_meihelp_backend.taxes.functions import fetch_das
from tcc_meihelp_backend.taxes.models import DAS


class DASViewset(viewsets.ViewSet):
    serializer_class = DasSerializer

    def get_queryset(self):
        company = self.request.user
        return DAS.objects.filter(company_id=company.id)

    @action(methods=['GET'], detail=False)
    def list_user_das(self, request):
        user = request.user
        das = self.get_queryset()

        if len(das) == 0:
            response = fetch_das(user.cnpj)
            if response['code'] != 200:
                return Response(status=response['code'])

            for das_data in response['data']:
                for periodo in das_data['periodos']:
                    data_periodo = das_data['periodos'][periodo]

                    das_periodo = {
                        'company_id': user,
                        'mes': int(periodo[4:6]),
                        'ano': int(periodo[0:4]),
                        'apurado': data_periodo['apurado'],
                        'situacao': data_periodo['situacao'] if len(data_periodo['situacao']) > 0 else 'Liquidado',
                        'principal': data_periodo['principal'],
                        'multa': data_periodo['multas'],
                        'juros': data_periodo['juros'],
                        'total': data_periodo['total'],
                        'data_vencimento': datetime.strptime(data_periodo['data_vencimento'], '%d/%m/%Y').strftime('%Y-%m-%d') if len(data_periodo['data_vencimento']) > 0 else None,
                        'data_acolhimento': datetime.strptime(data_periodo['data_acolhimento'], '%d/%m/%Y').strftime('%Y-%m-%d') if len(data_periodo['data_acolhimento']) > 0 else None,
                        'url_das': data_periodo['url_das'] if len(data_periodo['url_das']) > 0 else None,
                        'updated_at': datetime.now()
                    }

                    DAS(**das_periodo).save()

        else:
            last_das_fetched = das.last().updated_at.replace(tzinfo=None)

            if abs(last_das_fetched - datetime.now()).days > 1:
                response = fetch_das(user.cnpj)
                if response['code'] != 200:
                    return Response(status=response['code'])

                for das_data in response['data']:
                    for periodo in das_data['periodos']:
                        data_periodo = das_data['periodos'][periodo]

                        try:
                            das_filtered = DAS.objects.get(company_id=user, mes=int(periodo[4:6]), ano=int(periodo[0:4]))

                            das_filtered.apurado = data_periodo['apurado']
                            das_filtered.situacao = data_periodo['situacao'] if len(data_periodo['situacao']) > 0 else 'Liquidado'
                            das_filtered.principal = data_periodo['principal']
                            das_filtered.multa = data_periodo['multas']
                            das_filtered.juros = data_periodo['juros']
                            das_filtered.total = data_periodo['total']
                            das_filtered.data_vencimento = datetime.strptime(data_periodo['data_vencimento'], '%d/%m/%Y').strftime('%Y-%m-%d') if len(data_periodo['data_vencimento']) > 0 else None
                            das_filtered.data_acolhimento = datetime.strptime(data_periodo['data_acolhimento'], '%d/%m/%Y').strftime('%Y-%m-%d') if len(data_periodo['data_acolhimento']) > 0 else None
                            das_filtered.url_das = data_periodo['url_das'] if len(data_periodo['url_das']) > 0 else None
                            das_filtered.updated_at = datetime.now()

                            das_filtered.save()
                        except DAS.DoesNotExist:
                            return Response(status=404)

        das = self.get_queryset()

        serializer = DasSerializer(das, many=True)
        return Response(serializer.data)
