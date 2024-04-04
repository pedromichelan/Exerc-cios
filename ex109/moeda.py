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