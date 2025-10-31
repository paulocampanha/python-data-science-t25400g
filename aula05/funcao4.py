# Nesse programa vamos estudar o uso de funções com argumentos
# e com retorno
import math

# Funçao para calcular a área de um retângulo
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

# Função para calcular a área do círculo
def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

# Função para imprimir uma linha divisória
def linha():
    print()
    print('-' * 50)

print('----- Senai Celso Charuri -----')
print('Calculando a Área:')
linha()
base_retangulo = float(input('Digite a base do retângulo: '))
altura_retangulo = float(input('Digite a altura do retangulo: '))
print(f'A área do retâmgulo é \
{calcular_area_retangulo(base_retangulo, altura_retangulo)}')
linha()
raio_circulo = float(input('Digite o raio do círculo: '))
print(f'A área do circulo é \
    {calcular_area_circulo(raio_circulo):.2f}')
linha()
print('***** Fim do Programa *****')
