a = ('LÁPIS', 1.75, 'BORRACHA', 2.00, 'CADERNO', 15.90, 'ESTOJO', 25.00, 'TRANSFERIDOR', 4.20, 'COMPASSO', 9.99, 'MOCHILA', 120.32,
     'CANETA', 22.30, 'LIVRO', 34.90)
print(a)
print('-'*80)
#print('{:~^80}'.format(' LISTA DE PREÇOS '))
print(f'{" LISTA DE PREÇOS ":*^80}')
print('-'*80)
b = range(0, 18)
for x in b:
     if x % 2 == 0:
          print(f'{a[x]:.<71}', end='')
     if x % 2 == 1:
          print(f'R${a[x]:>7.2f}')
