# Nesse programa vamos calcular a idade de uma pessoa

import datetime
data_atual = datetime.date.today()
print(data_atual)
ano_atual = data_atual.year
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano_nascimento

resposta = input('Você já fez aniversário esse ano S/N: ')

if resposta.upper() == 'N':      # .upper() converte para muísculas
    idade -= 1     #  equivalente à idade = idade -1

print(f'Você tem {idade} anos.')


