# Sistema de agenda de contatos

agenda = {}
while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado à agenda.")

    elif escolha == "2":
        if len(agenda) == 0:
            print("A agenda está vazia.")
        else:
            print("Contatos na agenda:")
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")

    elif escolha == "3":
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    elif escolha == "4":
        print("Obrigado por usar a agenda de contatos. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        