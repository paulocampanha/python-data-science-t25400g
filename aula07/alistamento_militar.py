# Nesse programa vamos verificar se um jovem está apto para fazer o
# alistamento militar

print('=' * 30)
print('Exercíto Brasileiro')
print('=' * 30)
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('SEXO: Digite (M) para masculino ou (F) para feminino: ')

if idade == 18:
    if sexo.lower() == 'm':
        print('Você está apto para o serviço militar.')
        print('Dirija-se para uma junta militar.')

print('=' * 30)
print('Sistema Militar')