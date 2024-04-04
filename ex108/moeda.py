def aumentar(n=0, t=0):
    x = ((t+100)/100)*n
    return x

def diminuir(n=0, t=0):
    x = ((100-t) / 100) * n
    return x

def dobro(n=0):
    x = n*2
    return x

def metade(n=0):
    x = n/2
    return x

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')