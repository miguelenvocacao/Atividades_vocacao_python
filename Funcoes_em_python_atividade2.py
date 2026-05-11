# Sistema de conta das notas do aluno

# Função para calcular média
def calcular_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    print(f"\nMédia do aluno: {media:.2f}")

    if media >= 7:
        print("Aluno aprovado!")

    elif media >= 5:
        print("Aluno em recuperação!")

    else:
        print("Aluno reprovado!")


# Parte principal
print("=== CALCULADORA DE MÉDIA ===")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

calcular_media(n1, n2, n3)
