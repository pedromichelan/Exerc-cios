a = float(input('Qual o preço do produto?: R$'))
#desconto
b = float(input('Informe do desconto (%):'))
#desconto decimal
c = 1-(b/100)
print('Aplicando o desconto de {:.0f}% o valor final do produto será de R${:.2f}'.format(b, a*c))
