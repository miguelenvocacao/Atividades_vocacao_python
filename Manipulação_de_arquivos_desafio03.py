
# SISTEMA DE NOTAS


import csv
import os

ARQUIVO = "notas_alunos.csv"


# FUNÇÃO PARA ADICIONAR ALUNOS


def adicionar_aluno():

    nome = input("Digite o nome do aluno(a): ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    # VERIFICAR SE O ARQUIVO EXISTE
    arquivo_existe = os.path.isfile(ARQUIVO)

    # ABRE O ARQUIVO
    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        # ESCREVE O CABEÇALHO APENAS UMA VEZ
        if not arquivo_existe:
            escritor.writerow(["Nome", "Nota 1", "Nota 2", "Média"])

        # ESCREVE OS DADOS
        escritor.writerow([nome, nota1, nota2, media])

    print("\nAluno cadastrado com sucesso!\n")



# FUNÇÃO PARA MOSTRAR AS NOTAS


def mostrar_notas():

    # VERIFICAR SE O ARQUIVO EXISTE
    if not os.path.isfile(ARQUIVO):
        print("\nNenhum dado encontrado.\n")
        return

    print("\n=== NOTAS DOS ALUNOS ===\n")

    with open(ARQUIVO, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)

    print()



# MENU PRINCIPAL DO SISTEMA


while True:

    print("=== SISTEMA DE NOTAS ===")
    print("1 - Adicionar nota do aluno(a)")
    print("2 - Mostrar notas")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        mostrar_notas()

    elif opcao == "0":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida!\n")