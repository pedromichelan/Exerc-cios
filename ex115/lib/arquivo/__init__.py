from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('HOUVE UM ERRO NA CRIACAO DO ARQUIVO!')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO!')
    else:
        cabecalho('PESSOAS CADASTRADAS', 35)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15}{dado[1]:>15} ANOS')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('HOUVE UM ERRO NA ABERTURA DO ARQUIVO!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('HOUVE UM ERRO NA HORA DE ESCREVER OS DADOS!')
        else:
            print(f'NOVO REGISTRO DE {nome} CADASTRADO COM SUCESSO!')
            a.close()
