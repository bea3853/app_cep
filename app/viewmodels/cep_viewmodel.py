from app.models.cep_model import buscar_cep


def get_cep_data(cep):
    if not cep or not cep.isdigit() or len(cep) != 8:
        return {"erro": "CEP inválido"}

    data = buscar_cep(cep)

    if not data:
        return {"erro": "CEP não encontrado ou API indisponível"}

    # compatível com múltiplas APIs
    return {
        "logradouro": data.get("logradouro"),
        "bairro": data.get("bairro"),
        "cidade": data.get("localidade") or data.get("cidade"),
        "estado": data.get("uf") or data.get("estado")
    }