# Numeros pares e inpares

numeros = []

for i in range(5):
    n = int(input(f"Digite o número {i+1}: "))
    numeros.append(n)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
