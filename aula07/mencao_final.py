# Nesse programa vamos verificar a menção final do aluno e determinar
# se o mesmo foi aprovado, reprovado ou ficou de recuperação

mencao = input('Digite a menção do aluno (D, ED, ND): ')

if mencao.upper() == "D":
    print('O aluno está desenvolvido na matéria, \
        portanto está aprovado.')
elif mencao.upper() == "ED":
    print('O aluno está em desenvolvimento, \
        portanto está de recuperação')
elif mencao.upper() == "ND":
    print('O aluno não está desenvolvido, \
        portanto está reprovado')
else:
    print('Menção inválida.')