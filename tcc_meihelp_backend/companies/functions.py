from datetime import datetime

import requests


def fetch_cnpj(cnpj):
    try:
        response = requests.get('https://receitaws.com.br/v1/cnpj/' + cnpj)

        if response.status_code == 200:
            data = response.json()

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
