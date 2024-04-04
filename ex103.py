def ficha(nome='<desconhecido>', gols=0):
    """
    A FUNÇÃO RETORNA UMA FICHA COM OS DADOS DO JOGADOR
    :param nome: NOME DO JOGADOR
    :param gols: NÚMERO DE GOLS (INTEIRO)
    :return: FICHA
    """
    return f'O JOGADOR {nome} FEZ {gols} GOL(S) NO CAMPEONATO.'


#PROGRAMA PRINCIPAL
a = str(input('NOME DO JOGADOR: '))
b = input('GOLS MARCADOS: ')
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    print(ficha(gols=b))
else:
    print(ficha(a, b))
