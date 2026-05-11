# Sistema que determina qual é o maior e menor número

def maior_menor(lista):

    maior = max(lista)
    menor = min(lista)

    return maior, menor


# Lista de números
numeros = []

quantidade = int(input("Quantos números deseja adicionar? "))

for i in range(quantidade):

    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)


# Chamada da função
maior, menor = maior_menor(numeros)

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")