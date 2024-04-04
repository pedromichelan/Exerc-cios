from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['MOSTRAR LISTA', 'CADASTRAR NOVO', 'SAIR DO SISTEMA'], 'MENU PRINCIPAL', 35)
    if resp == 1:
        lerArquivo(arq)
    elif resp ==2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('SAINDO DO SISTEMA ... ATÉ LOGO!')
        print(linha(35))
        break
    else:
        print('\33[31mDIGITE UMA OPÇÃO VÁLIDA!\33[m')
        sleep(1.5)
