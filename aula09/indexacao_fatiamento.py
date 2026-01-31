# Nesse programa vamos usar o indice de cada elemento para fatiar
# o array e o vetor (matriz) extraindo seus elementos
import numpy as np

dados_1d = np.array([10, 20, 30, 40, 50, 60])
dados_2d = np.array([
    [110, 120, 130],
    [220, 230, 240],
    [330, 340, 350]
])

# Primeiro elemento
primeiro_elemento_1d = dados_1d[0]
print(f"Primeiro elemento 1d: {primeiro_elemento_1d}")

primeiro_elemento_2d = dados_2d[0, 0]
print(f"Primeiro elemento 2d: {primeiro_elemento_2d}")

# ùltimo elemento
ultimo_elemento_1d = dados_1d[-1]
print(f"Último elemento 1d: {ultimo_elemento_1d}")

ultimo_elemento_2d = dados_2d[-1, -1]
print(f"Último elemento 2d: {ultimo_elemento_2d}")

# Fatiamento
fatia_basica_1d = dados_1d[1:4]
print(f"Elementos do 2 até o 4: {fatia_basica_1d}")

fatia_basica_2d = dados_2d[0:2, 1:3]
print(f"Linha 0 até 1 e coluna 1 até 2: {fatia_basica_2d}")

fatia_inicio_1d = dados_1d[:3]
print(f"Do inicio até indice 2: {fatia_inicio_1d}")

fatia_inicio_2d = dados_2d[:2, :2]
print(f"Do inicio até indice 1: {fatia_inicio_2d}")

fatia_fim_1d = dados_1d[2:]
print(f"Do índice 2 até o final: {fatia_fim_1d}")

fatia_fim_2d = dados_2d[1:, 1:]
print(f"Do índice 1 até o final: {fatia_fim_2d}")

fatia_passo_1d = dados_1d[::2]
print(f"A cada dois elementos: {fatia_passo_1d}")

fatia_passo_2d = dados_2d[::2, ::2]
print(f"A cada dois elementos: {fatia_passo_2d}")

array_invertido = dados_1d[::-1]
print(f"Array invertido: {array_invertido}")

matriz_invertida = dados_2d[::-1, ::-1]
print(f"Matriz invertida: {matriz_invertida}")

