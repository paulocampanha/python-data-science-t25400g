# Nesse programa vamos criar um arquivo texto usando a programação
# do Python
# 'a' cria um arquivo novo. Se o arquvo existir, o mesmo será aberto
# e o conteúdo e gravado no final do arquivo


def gravar_texto(nome_arquivo, texto):

    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo: 
        arquivo.write(texto + '\n')
        print('Conteudo gravado com sucesso')

nome_arquivo = 'texto2.txt'
texto = 'Unidade Guarulhos'

gravar_texto(nome_arquivo, texto)
