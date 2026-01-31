# Nesse programa vamos conhecer os comando basicos da biblioteca 
# numpy e assim verificar se a instalação foi bem sucedida

import numpy as np

# lista criada com o python
lista = [100, 200, 300, 400, 500]

# lista criada com o numpy
dados_1d = np.array([10, 20, 30, 40, 50])

print(f"Lista do Python: {lista}")
print(f"Array do Numpy: {dados_1d}")

# Matriz criada com o numpy
dados_2d = np.array([
    [5, 10, 15],
    [3, 6, 9],
    [7, 14, 21]
])

print(f"Matriz do Numpy: {dados_2d}")

# Função para criar um array de 0s
array_zeros = np.zeros(6)
print(f"Array de Zeros: {array_zeros}")
array_zeros[0] = 15
array_zeros[2] = 25
array_zeros[5] = 125
print(f"Array de Zeros alterada: {array_zeros}")
array_zeros[1] += 75
print(f"Array de Zeros alterada 2: {array_zeros}")

# Função para criar um array de 1s
array_uns = np.ones(6)
print(f"Array de Uns: {array_uns}")

# Criando matrizes de 0s e 1s
matriz_zeros = np.zeros((5, 5))
print(f"Matriz de Zeros (5x5): {matriz_zeros}")

matriz_uns = np.ones((4, 3))
print(f"Matriz de Uns (4X3): {matriz_uns}")

# Função para criar uma array com números sequênciais
sequencia_1 = np.arange(10)  
print(f"Sequência 1: {sequencia_1}")  #Saída: [0 1 2 3 4 5 6 7 8 9]

sequencia_2 = np.arange(5, 11)
print(f"Sequência 2: {sequencia_2}") #Saída: [5 6 7 8 9 10]

sequencia_3 = np.arange(3, 31, 3)
print(f"Sequência 3: {sequencia_3}")  #Saída: [3 6 9 12 15 18 ... 30]

# Função para criar um array com valores igualmente espaçados
array_espacado1 = np.linspace(0, 10, 5)
print(f"Array com espaçamento 5: {array_espacado1}")

array_espacado2 = np.linspace(0, 1, 6)
print(f"Arrayc om espeçamento 6: {array_espacado2}")

# Função para criar array de números aleatórios
array_numeros_aleatorios1 = np.random.rand(5)
print(f"Array números aleatórois: {array_numeros_aleatorios1}")

matriz_numeros_aleatorios1 = np.random.rand(3, 2)
print(f"Matriz números aleatórios: {matriz_numeros_aleatorios1}")

array_numeros_aleatorios2 = np.random.randint(1, 60, 6)
print(f"Array números aleatórios: {array_numeros_aleatorios2}")


