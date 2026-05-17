# SISTEMA DE ESCOLA - PT1

from util.menu import menu_principal
from alunos.cadastro import cadastrar_aluno
from alunos.consulta import listar_alunos
from professores.notas import lancar_notas
from alunos.boletim import mostrar_boletim

print("=== SISTEMA ESCOLAR ===")

while True:

    menu_principal()

    opcao = input("\nEscolha: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        lancar_notas()

    elif opcao == "4":
        mostrar_boletim()

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")