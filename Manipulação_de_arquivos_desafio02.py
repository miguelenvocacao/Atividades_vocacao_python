# Dicionário em JSON

import json

# Dicionário de clientes

clientes = {
    "cliente1": {
        "nome": "Vocação",
        "idade": 50,
        "cidade": "São Paulo"
    },
    "cliente2": {
        "nome": "Ana",
        "idade": 25,
        "cidade": "Rio de Janeiro"
    },
    "cliente3": {
        "nome": "Carlos",
        "idade": 30,
        "cidade": "Curitiba"
    }
}

# Salvar em JSON

with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

print("Dados salvos no arquivo clientes.json!")

# Carregar arquivo JSON

with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

# Exibir dados

print("\n=== CLIENTES CADASTRADOS ===")

for chave, cliente in dados_carregados.items():
    print(f"\n{chave}")
    print(f"Nome: {cliente['nome']}")
    print(f"Idade: {cliente['idade']}")
    print(f"Cidade: {cliente['cidade']}")