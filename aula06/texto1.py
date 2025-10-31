# Nesse programa vamos criar um arquivo texto usando a programação
# do Python
# 'w' cria um arquivo novo para receber um conteúdo. Se o arquivo
# existir, ele é substituido pelo novo arquivo

def gravar_texto_em_arquivo(nome_arquivo, texto):

    with open(nome_arquivo, 'w') as arquivo:  
        arquivo.write(texto)

nome_do_arquivo = 'texto1.txt'
conteudo_do_arquivo = 'Menininha quando dorme, poem a mão no coração.'

gravar_texto_em_arquivo(nome_do_arquivo, conteudo_do_arquivo)