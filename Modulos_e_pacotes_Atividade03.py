# JOGO DE ADIVINHAÇÃO

import random
import math

print("=== JOGO DE ADIVINHAÇÃO ===")

# GERA UM NÚMERO ALEATÓRIO
numero_secreto = random.randint(1, 100)

tentativas = 0

while True:

    # PEDE UM NÚMERO AO JOGADOR
    palpite = int(input("\nDigite um número entre 1 e 100: "))

    tentativas += 1

    # CALCULA A DIFERENÇA (USANDO O MATH)
    diferenca = math.fabs(numero_secreto - palpite)

    # VERIFICAÇÕES
    if palpite == numero_secreto:

        print("\n🎉 PARABÉNS! VOCÊ ACERTOU!")
        print(f"O número secreto era {numero_secreto}")
        print(f"Total de tentativas: {tentativas}")
        break

    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.")

    else:
        print("O número secreto é MENOR.")

    # DICAS DE DISTÂNCIA
    if diferenca <= 5:
        print("🔥 Muito perto!")

    elif diferenca <= 15:
        print("😎 Perto!")

    else:
        print("❄️ Muito longe!")