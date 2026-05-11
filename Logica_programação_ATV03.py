# Sitstema que recebe a idade do usuario e estima ela

# Solicitar a idade do usuario
print("Olá! Digite sua idade para estimar ela:")
idade = int(input("Digite sua idade: "))
# Estimar a idade do usuario

if idade < 0:
    print("Idade inválida. Por favor, digite uma idade válida.")
elif idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Sistema que estimula sua idade futura
print("Deseja saber sua idade futura? (sim/não)")
resposta = input().lower()
if resposta == "não":
    print("Obrigado por usar o sitema, volte sempre!")

if resposta == "sim":
    anos = int(input("Quantos anos você quer adicionar? "))
    idade_futura = idade + anos
    print(f"Você terá {idade_futura} anos em {anos} anos.")
