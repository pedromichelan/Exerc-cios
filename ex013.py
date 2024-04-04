a = float(input('Qual o salário atual do funcionário?: R$'))
#reajuste
b = float(input('Informe o reajuste (%):'))
#reajuste decimal
c = 1+(b/100)
print('Com o reajuste de {:.0f}% o valor final do salário desse funcionário será de R${:.2f}'.format(b, a*c))
