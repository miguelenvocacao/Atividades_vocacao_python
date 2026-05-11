# Lista interativas de compras


lista = []

while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista.append(item)  
        print(f"{item} adicionado à lista de compras.")

    elif escolha == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista: 
            lista.remove(item)
            print(f"{item} removido da lista de compras.")
        else:
            print(f"{item} não encontrado na lista de compras.")

    elif escolha == "3":
        if len(lista) == 0: 
            print("A lista de compras está vazia.")
        else:
            print("Lista de compras:")
            for item in lista:
                print(f"- {item}")

    elif escolha == "4":
        print("Obrigado por usar a lista de compras. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")