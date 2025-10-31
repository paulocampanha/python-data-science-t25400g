# Nesse programavamos verificar a temperatura informada e imprimir 
# uma classificação. Para isso vamos utilizar a Comparação Encadeada


temperatura = float(input('Digite a temperatura atual: '))

if temperatura <= 0:
    print('Hoje está congelante.')
elif 0 < temperatura <= 10:   # temjperatura entre 0 e 10
    print('Hoje está muito frio') 
elif 10 < temperatura <= 20:
    print('Hoje está frio')
elif 20 < temperatura <= 26:
    print('Hoje está agradável.')
else:
    print('Hoje está muito quente.')