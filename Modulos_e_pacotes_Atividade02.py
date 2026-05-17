# GERADOR DE INFORMAÇÕES FALSAS

from faker import Faker
import random

# DEFINIR IDIOMA
fake = Faker("pt_BR")

print("=== GERADOR DE CLIENTES FALSOS ===\n")

# GERANDO QUANTIDADE ALEATÓRIA DE CLIENTES
quantidade = random.randint(1, 10)

print(f"\n=== GERANDO {quantidade} CLIENTES ===\n")

for i in range(quantidade):

    nome = fake.name()
    email = fake.email()
    telefone = fake.phone_number()
    cidade = fake.city()

    print(f"Cliente {i+1}")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")
    print(f"Cidade: {cidade}")
    print("-" * 30)