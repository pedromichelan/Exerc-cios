print(f'{" MONTANDO MATRIZ 3X3 ":*^50}')
a = [[], [], []]
for x in range(0, 3):
    b = 0
    while b <= 2:
        a[x].insert(b, int(input(f'DIGITE UM VALOR PARA [{x}, {b}]: ')))
        b += 1
print(f'[ {a[0][0]} ] [ {a[0][1]} ] [ {a[0][2]} ]')
print(f'[ {a[1][0]} ] [ {a[1][1]} ] [ {a[1][2]} ]')
print(f'[ {a[2][0]} ] [ {a[2][1]} ] [ {a[2][2]} ]')
