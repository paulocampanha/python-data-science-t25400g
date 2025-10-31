# Crie uma lista chamada numeros com os valores 10, 20, 30, 
# 40 e 50. Imprima a lista completa. 
# Adicione o número 60 no final da lista e o número
# 25 entre o 20 e o 30. Imprima a lista completa.
# Remova o número 10 e o 40. Imprima a lista completa.
numeros = [10, 20, 30, 40, 50]
print(f'Lista de números: {numeros}')
numeros.append(60)
numeros.insert(2, 25)
print(f'Lista de números após a inserção: {numeros}')
numeros.remove(10)
numeros.remove(40)
print(f'Lista de números após a remoção: {numeros}')
print('=' * 50)

# Crie uma lista de cores vazia. Solicite ao usuário para digitar
# três cores e insira cada cor na lista. Imprima a lista completa.
cores = []
cor = input('Digite uma cor: ')
cores.append(cor)
cor = input('Digite outra cor: ')
cores.append(cor)
print(f'Lista de cores: {cores}')
print('=' * 50)
# Crie uma lista de letras com as letras: a, b, c, d, e, f, g e h.
# Imprima a lista completa.
# Imprima o fatiamento da lista de acordo com: 
# - 3 primeiras letras;
# - 3 últimas letra; 
# - as 2 letras do meio da lista.
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(f'Letras: {letras}')
print(f'Três primeiras letras: {letras[:3]}')
print(f'Três últimas letras: {letras[-3:]}')
print(f'As 2 letras do meio: {letras[3:5]}')
