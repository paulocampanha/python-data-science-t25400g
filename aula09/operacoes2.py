# Nesse programa vamos executar mais operações matemáticas com
# arrays
import numpy as np

array_a = np.array([1, 2, 3])
array_b = np.array([10, 20, 30])

soma = array_a + array_b
print(f"Soma das arrays: {soma}")
multi = array_a * array_b
print(f"Multiplicação das arrays: {multi}")
potencia = array_a ** 2
print(f"Array_a elevado a 2: {potencia}")
raiz = np.sqrt(array_b)
print(f"Raiz de array_b: {raiz}")



