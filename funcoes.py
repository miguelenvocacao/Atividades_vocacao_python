# IMPORT DE UTILIDADES

import utilidades

# ENTRADA DE DADOS
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# UTILIZANDO AS FUNÇÕES
print("\n=== RESULTADOS ===")
print("Soma:", utilidades.soma(num1, num2))
print("Subtração:", utilidades.subtracao(num1, num2))
print("Multiplicação:", utilidades.multiplicacao(num1, num2))
print("Divisão:", utilidades.divisao(num1, num2))
print("Potência:", utilidades.potencia(num1, num2))