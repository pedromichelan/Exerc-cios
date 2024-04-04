print(f'{" FORMAÇÃO DE LISTA ":+^50}')
b = [ ]
for x in range(1, 6):
    a = int(input('DIGITE UM VALOR PARA A POSIÇÃO {}: '.format(x)))
    b.append(a)
print(b)
c = 0 #menor valor
d = 0 #maior valor
for y in range(0, 5):
    if y == 0:
        c = b[y]
        d = b[y]
    else:
        if b[y] < c:
            c = b[y]
        if b[y] > d:
            d = b[y]
print(f'O MENOR VALOR DIGITADO FOI {c} NAS POSIÇÕES: ', end='')
for i, v in enumerate(b):
    if v == c:
        print(f'{i}..', end='')
print(f'\nO MAIOR VALOR DIGITADO FOI {d} NAS POSIÇÕES: ', end='')
for i, v in enumerate(b):
    if v == d:
        print(f'{i}..', end='')
