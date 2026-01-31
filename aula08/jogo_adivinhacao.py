# Nesse programa vamos criar um jogo onde o jogador terá três chances
# de acertar um número sorteado pelo conputador. Para cada erro do 
# jogar, o computador deve dar uma dica informando se o seu paplpite
# é um número menor ou maior do que o número sorteado.

import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

while tentativas < 3:
    palpite = int(input("Digite seu palpite entre 1 e 10: "))
    tentativas += 1
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor do que seu palpite.")
    else:
        print("O número secreto é maior do que seu palpite.")

if acertou:
    print("PARABÉNS! Você acertou o número secreto.")
else:
    print("PERDEU! Você não acertou o número secreto.")
    print(f"O número sorteado foi {numero_secreto}")