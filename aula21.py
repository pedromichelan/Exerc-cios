def contador(i, f, p):
    """ Função para contagem de um número inicial até um número final com o passo p
    :param i: número inicial
    :param f: número final
    :param p: passo de p em p
    :return: a lista de números
    """
    for x in range(i, f+1, p):
        print(x, end=' ')




def somar(a=0, b=0, c=0):
    """
    A FUNÇÃO SOMAR RETORNA A SOMA DE TRÊS NÚMEROS INFORMADOS, SENDO O VALOR PADRÃO PARA ELES ZERO.
    :param a: 
    :param b: 
    :param c: 
    :return: 
    """
    s = a+b+c
    return s


r1 = somar(5, 6, 9)
r2 = somar(1, 4)
r3 = somar(9)
#print(f'AS SOMAS DERAM {r1}, {r2} E {r3}')


def funcao():
    n1 = 5
    print(f'N1 dentro vale {n1}')


n1 = 8
#print(f'N1 fora vale {n1}')

def teste(b):
    global a
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
#teste(a)


def fatorial(n=1, s=False):
    """
    RETORNA O FATORAL DO NÚMERO INFORMADO
    :param n: NÚMERO INICIAL
    :param s: MOSTRA A CONTA False É PADRÃO
    :return:
    """
    c = a = n
    if s == True:
        for x in range(n-1, 0, -1):
            print(f'{c} X ', end='')
            c -= 1
            a *= x
        print(c)
    if s == False:
        for x in range(n-1, 0, -1):
            a *= x
    return a


print(fatorial(5))
