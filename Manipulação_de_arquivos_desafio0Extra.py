
# SISTEMA DE BACKUP AUTOMÁTICO

import shutil
import os

# PASTA DE ORIGEM (ARQUIVOS IMPORTANTES)
pasta_origem = "arquivos_importantes"

# PASTA DE DESTINO (BACKUP)
pasta_backup = "backup"


# CRIAR AS PASTAS CASO NÃO EXISTAM


os.makedirs(pasta_origem, exist_ok=True)
os.makedirs(pasta_backup, exist_ok=True)


# FUNÇÃO DE BACKUP

def fazer_backup():

    arquivos = os.listdir(pasta_origem)

    # VERIFICAR SE EXISTEM ARQUIVOS
    if not arquivos:
        print("\nNenhum arquivo encontrado para o backup.\n")
        return

    print("\nIniciando backup...\n")

    for arquivo in arquivos:

        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_backup, arquivo)

        # COPIAR O ARQUIVO
        shutil.copy2(caminho_origem, caminho_destino)

        print(f"Arquivo copiado: {arquivo}")

    print("\nBackup concluído com sucesso!\n")



# MENU PRINCIPAL


while True:

    print("=== SISTEMA DE BACKUP ===")
    print("1 - Fazer backup")
    print("2 - Ver arquivos da pasta origem")
    print("3 - Ver arquivos da pasta backup")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # FAZER BACKUP
    if opcao == "1":
        fazer_backup()

    # MOSTRAR ARQUIVOS DA ORIGEM
    elif opcao == "2":

        arquivos = os.listdir(pasta_origem)

        print("\n=== ARQUIVOS ORIGINAIS ===")

        if arquivos:
            for arquivo in arquivos:
                print("-", arquivo)
        else:
            print("Nenhum arquivo encontrado.")

        print()

    # MOSTRAR ARQUIVOS DO BACKUP
    elif opcao == "3":

        arquivos = os.listdir(pasta_backup)

        print("\n=== ARQUIVOS DO BACKUP ===")

        if arquivos:
            for arquivo in arquivos:
                print("-", arquivo)
        else:
            print("Nenhum arquivo encontrado.")

        print()

    # ENCERRAR SISTEMA
    elif opcao == "0":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida!\n")