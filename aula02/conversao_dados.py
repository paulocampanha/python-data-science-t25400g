# Nesse programa vamos estudar a conversão de dados em python
# A connversão permite alterar o tipo de dados de uma variável
# para outro tipo de dados. Por exemplo, uma variavel do tipo texto
# pode ser convertida para número, desde que seu valor seja um 
# numero. 
# idade = '18' -> Essa variável, apesar de ter um número é considerada
# pelo Python como um texto (string), pois o número se encontra entre
# aspas. Para converter essa variável para número usamos a função int()

idade_str = '18'
print(f'A variável idade_str é do tipo {type(idade_str)}.')
idade_int = int(idade_str)
print(f'A variável idade_int é do tipo {type(idade_int)}.')
soma = idade_int + 10
print(f'Resultado: {soma}.')
