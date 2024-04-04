def aumentar(n=0, t=0, m=True):
    x = ((t+100)/100)*n
    if m == False:
        return x
    if m == True:
        return moeda(x)


def diminuir(n=0, t=0, m=True):
    x = ((100-t) / 100) * n
    if m == False:
        return x
    else:
        return moeda(x)

def dobro(n=0, m=True):
    x = n*2
    if m == False:
        return x
    else:
        return moeda(x)

def metade(n=0, m=True):
    x = n/2
    if m == False:
        return x
    else:
        return moeda(x)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(p=0, a=0, d=0):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"PREÇO ANALISADO:":<25}{moeda(p):>10}')
    print(f'{"DOBRO DO PREÇO:":<25}{dobro(p, True):>10}')
    print(f'{"METADE DO PREÇO:":<25}{metade(p, True):>10}')
    print(f'{a:<4}{"% DE AUMENTO:":<21}{aumentar(p, a, True):>10}')
    print(f'{d:<4}{"% DE DESCONTO:":<21}{diminuir(p, d, True):>10}')
    print('-' * 35)
