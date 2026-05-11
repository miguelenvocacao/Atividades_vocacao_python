# Sistema de cadastro e login

# Dicionário para armazenar usuários
usuarios = {}


# Função para criar conta
def criar_conta():

    print("\n=== CRIAR CONTA ===")

    usuario = input("Crie um nome de usuário: ")
    senha = input("Crie uma senha: ")

    usuarios[usuario] = senha

    print("\nConta criada com sucesso!")


# Função para fazer login
def fazer_login():

    print("\n=== LOGIN ===")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:

        print(f"\nLogin realizado com sucesso!")
        print(f"Bem-vindo(a), {usuario}!")

    else:

        print("\nUsuário ou senha incorretos!")


# Menu principal
while True:

    print("\n=== SISTEMA ===")

    print("1 - Criar conta")
    print("2 - Fazer login")
    print("0 - Sair")

    escolha = input("\nEscolha: ")

    if escolha == "1":

        criar_conta()

    elif escolha == "2":

        fazer_login()

    elif escolha == "0":

        print("\nSaindo do sistema...")
        break

    else:

        print("\nOpção inválida!")

















