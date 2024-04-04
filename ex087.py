print(f'{" ANÁLISE DE MATRIZES 3X3 ":-^50}')
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = 0 #soma pares
c = 0 #soma terceira coluna
#d = 0 #maior segunda linha
for x in range(0, 3):
    for y in range(0, 3):
        a[x][y] = int(input(f'DIGITE UM VALOR PARA [{x}, {y}]: '))
        if a[x][y] % 2 == 0:
            b += a[x][y]
        if y == 2:
            c += a[x][y]
d = max(a[1])
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{a[x][y]:^5}]', end='')
    print()
print(b)
print(c)
print(d)
