import requests

def consultar_cep(cep: str):
    cep = ''.join(filter(str.isdigit, cep))
    r = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
    d = r.json()
    if d.get("erro"):
        return None
    return d
