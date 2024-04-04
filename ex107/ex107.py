import moeda
n = int(input('DIGITE O VALOR: '))
print(f'{n} aumentado é {moeda.aumentar(n, 10):.1f}')
print(f'{n} diminuido é {moeda.diminuir(n, 50):.1f}')
print(f'{n} dobrado é {moeda.dobro(n):.1f}')
print(f'A metade de {n} é {moeda.metade(n):.1f} ')
