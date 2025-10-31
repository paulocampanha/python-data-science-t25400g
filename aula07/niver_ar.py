# Nesse programa vamos usar mais de desvio condicional para verificar
# a situação do ar em relação a temperatura e umidade

temperatura = int(input('Digite a temperatura atual: '))
umidade = int(input('Digite o nivel de umidade atual: '))
risco_saude = False

if temperatura >= 40:
    print('Temperatura muito alta para o ser humano.')
    risco_saude = True

if umidade <= 40 or umidade >= 60:  # operador lógico or (ou)
    print('Umidade muita baixa ou muita alta para o ser humano.')
    risco_saude = True

if risco_saude:
    print('A temperatura ou a Umidade não estão adequadas para o ser humanao')