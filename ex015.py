#R$60,00/dia
#R$0,15/km rodado
a = int(input('Digite quantos dias o carro ficou alugado:'))
b = int(input('Digite quantos quilometros foram rodados com o carro:'))
d = int(input('Digite qual o valor da diária de acordo com a tabela:'))
k = float(input('Digite qual o valor do Km rodado de acordo com a tabela:'))
print('O total a pagar é: R${:.2f}'.format(a*d+b*k))
