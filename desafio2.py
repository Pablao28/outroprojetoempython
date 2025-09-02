import random

numero_secreto = 42
max_tentativas = 5
print("Bem-vindo ao Jogo da Adivinhação! Você tem 5 tentativas.")

for tentativa in range(1, max_tentativas + 1):
    print(f"Tentativa {tentativa} de {max_tentativas}")
    try:
        chute = int(input("Digite o seu palpite: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns!")
        break
    elif maior:
        print("O número secreto é menor.")
    elif menor:
        print("O número secreto é maior.")

if not acertou:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")