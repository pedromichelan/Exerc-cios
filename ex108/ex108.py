import moeda
n = int(input('DIGITE O VALOR: R$'))
print(f'{moeda.moeda(n)} aumentado é {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'{moeda.moeda(n)} diminuido é {moeda.moeda(moeda.diminuir(n, 50))}')
print(f'{moeda.moeda(n)} dobrado é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))} ')
