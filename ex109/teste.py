import moeda
n = int(input('DIGITE O VALOR: R$'))
print(f'{moeda.moeda(n)} aumentado 10% é {moeda.aumentar(n, 10, m=True)}')
print(f'{moeda.moeda(n)} diminuido 50% é {moeda.diminuir(n, 50, m=True)}')
print(f'{moeda.moeda(n)} dobrado é {moeda.dobro(n)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)} ')
