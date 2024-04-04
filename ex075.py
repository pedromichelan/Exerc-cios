a = (int(input('DIGITE UM VALOR: ')),
     int(input('DIGITE UM VALOR: ')),
     int(input('DIGITE UM VALOR: ')),
     int(input('DIGITE UM VALOR: ')), )
print(a)
print(f'O NÚMERO 9 APARECEU {a.count(9)} VEZES')
if 3 in a:
    print(f'O VALOR 3 APARECEU NA {a.index(3)+1}º POSIÇÃO')
else:
    print('O VALOR 3 NÃO FAZ PARTE DO CONJUNTO')
print(('OS VALORES DIGITADOS FORAM: '), end='')
for x in a:
    if x % 2 == 0:
        print(x, sep=' e ')
        print(end='')
