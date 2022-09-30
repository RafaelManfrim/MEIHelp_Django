import requests
from django.conf import settings


def fetch_das(cnpj):
    infosimples_token = settings.INFOSIMPLES_TOKEN

    url = 'https://api.infosimples.com/api/v2/consultas/receita-federal/simples-das'

    args = {
        "cnpj": cnpj,
        "token": infosimples_token,
        "timeout": 600
    }

    response = requests.post(url, args)
    response_json = response.json()

    return response_json
