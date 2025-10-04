# Nesse programa vamos manipular as listas com comandos
# de alteração, inserção e remoção.

# Lista vazia de frutas
frutas = []
#inserindo um item na lista
frutas.append('maçã')
print(frutas)
fruta = input('Digite sua fruta favorita: ')
frutas.append(fruta)
print(frutas)
frutas.append('banana')
print(frutas)
frutas.insert(0, 'acerola')
print(frutas)
fruta = input('Digite outra fruta: ')
frutas.insert(3, fruta)
print(frutas)
frutas[1] = 'pera'
print(frutas)
frutas.pop()
print(frutas)
frutas.pop(0)
print(frutas)
frutas.remove('pera')
print(frutas)

