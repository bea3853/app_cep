import requests
from config import BASE_URL, FALLBACK_URL


def buscar_cep_api_principal(cep):
    try:
        response = requests.get(
            f"{BASE_URL}{cep}",
            headers={"Accept": "application/json"},
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


def buscar_cep_fallback(cep):
    try:
        response = requests.get(
            f"{FALLBACK_URL}{cep}/json/",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


def buscar_cep(cep):
    # tenta API principal
    data = buscar_cep_api_principal(cep)

    if data:
        return data

    # fallback automático
    return buscar_cep_fallback(cep)