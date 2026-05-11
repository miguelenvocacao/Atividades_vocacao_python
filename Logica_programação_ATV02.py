# Programa para comparar dois numeros

# Solicitar dois numeros ao usuario

print("Ola! Digite dois numeros para comparar:")
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

# Comparar os numeros e mostrar o resultado

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num2} é maior que {num1}")
else:
    print("Os numeros são iguais")

