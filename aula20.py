'''def msg(x):
    print('-'*30)
    print(x)
    print('-' * 30)


msg('OLÁ MUNDO!')'''

'''a = 2
b = 4
s = a + b
print(s)'''


'''def soma(a, b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A SOMA É {s}!')

#programa principal
soma(b=10, a=0)'''

'''def somador(*num):
    x = 0
    for y in num:
        x += y
    print(f'O TOTAL É {x}!')


somador(4, 5, 9, 10, 33)'''


'''def contador(*num):
    tam = len(num)
    print(f'VOCÊ DIGITOU OS VALORES {num} E AO TODO SÃO {tam} NÚMEROS')

contador(3, 4, 5, 6)
contador(2, 1)'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 4, 6, 9]
dobra(valores)
print(valores)
