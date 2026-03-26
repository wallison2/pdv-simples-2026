import requests

SERVER_URL = "http://192.168.1.100:8000"  # IP do servidor local

def buscar_estoque():
    response = requests.get(f"{SERVER_URL}/estoque")
    if response.status_code == 200:
        return response.json()["estoque"]
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def buscar_usuarios():
    response = requests.get(f"{SERVER_URL}/usuarios")
    if response.status_code == 200:
        return response.json()["usuarios"]
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def registrar_transacao(tipo, valor, descricao):
    transacao = {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao
    }
    response = requests.post(f"{SERVER_URL}/transacoes", json=transacao)
    if response.status_code == 200:
        print("Transação registrada com sucesso")
    else:
        print(f"Erro: {response.status_code} - {response.text}")

# Exemplo de uso
estoque = buscar_estoque()
print("Estoque disponível:", estoque)
