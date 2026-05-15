# Sistema de gravação e leitura de arquivos TXT

print("=== SISTEMA DE ARQUIVO TXT ===")

# O usuário deve digitar uma mensagem
mensagem = input("Digite uma informação para salvar no arquivo: ")

# Criando e escrevendo uma mensagem
arquivo = open("informacoes.txt", "w", encoding="utf-8")

arquivo.write(mensagem)

arquivo.close()

print("\nInformação salva com sucesso!")

# Lendo o arquivo
arquivo = open("informacoes.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

arquivo.close()

# Exibindo o conteúdo
print("\n=== CONTEÚDO DO ARQUIVO ===")
print(conteudo)






















