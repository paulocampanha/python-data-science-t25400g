# Nesse programa vamos estudar funções sem argumento
# e com retorno.

import random

def sortear_numero():
    numero_sorteado = random.randint(1, 60)
    return numero_sorteado

print("----- Lotérica Pé de Coelho -----")
print("Sorteio do bolão da megasena")
numero = sortear_numero()
print(f'Número sorteado: {numero}' )
numero = sortear_numero()
print(f'Número sorteado: {numero}')
numero = sortear_numero()
print(f'Número sorteado: {numero}')
numero = sortear_numero()
print(f'Número sorteado: {numero}')
numero = sortear_numero()
print(f'Número sorteado: {numero}')
numero = sortear_numero()
print(f'Número sorteado: {numero}')
numero = sortear_numero()
print(f'Número sorteado: {numero}')