# Calculadora simples em Python
print("Bem-vindo à calculadora simples!")

# Entrada de dados

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
    
# Escolha da operação
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. porcemtagem")
operacao = input("Digite o número da operação desejada: ")

# Realização da operação
if operacao == "1":
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "2":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "3":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
elif operacao == "5":
        resultado = (num1 / num2) * 100
        print(f"O resultado da divisão é: {resultado}%")
else:
        print("Erro: Divisão por zero não é permitida.")
        print("Operação inválida. Por favor, escolha uma operação válida.")


