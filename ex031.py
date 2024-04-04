a = float(input('DIGITE A DISTÂNCIA DA VIAGEM:'))
b = 0.45
c = 0.50
if a < 200:
    print('O PREÇO DA PASSAGEM É: R${:.2f}'.format(a*c))
else:
    print('O PREÇO DA PASSAGEM É: R${:.2f}'.format(a*b))
