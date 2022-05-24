import requests
from datetime import datetime

from rest_framework import status

from tcc_meihelp_backend.companies.models import CNPJ


def fetch_cnpj(cnpj):
    try:
        response = requests.get('https://receitaws.com.br/v1/cnpj/' + cnpj)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ERROR':
                return None, 400

            cnpj_data = {
                'cnpj': cnpj,
                'updated_at': datetime.now()
            }

            if data['natureza_juridica'].startswith('213-5') and data['situacao'] == 'ATIVA':
                cnpj_data['is_mei'] = True
            else:
                cnpj_data['is_mei'] = False

            return cnpj_data, response.status_code

        if response.status_code == 429 or response.status_code == 504:
            return None, response.status_code

    except requests.exceptions.RequestException:
        return None, 500


def validate_cnpj(request_cnpj):
    # Pode retornar 200, 400, 401, 429, 500 e 504
    try:
        cnpj = CNPJ.objects.get(cnpj=request_cnpj)

        last_cnpj_fetch = cnpj.updated_at.replace(tzinfo=None)

        if abs((last_cnpj_fetch - datetime.now()).days) > 30:
            novos_dados, status_code = fetch_cnpj(request_cnpj)
            if status_code == status.HTTP_200_OK:
                cnpj.updated_at = novos_dados['updated_at']
                cnpj.is_mei = novos_dados['is_mei']
                cnpj.save()

                if cnpj.is_mei:
                    return status.HTTP_200_OK
                else:
                    return status.HTTP_401_UNAUTHORIZED
            else:
                return status_code

        else:
            if cnpj.is_mei:
                return status.HTTP_200_OK
            else:
                return status.HTTP_401_UNAUTHORIZED

    except CNPJ.DoesNotExist:
        novos_dados, status_code = fetch_cnpj(request_cnpj)
        if status_code == status.HTTP_200_OK:
            novo_cnpj = CNPJ.objects.create(**novos_dados)

            if novo_cnpj.is_mei:
                return status.HTTP_200_OK
            else:
                return status.HTTP_401_UNAUTHORIZED
        else:
            return status_code
