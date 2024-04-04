print('\033[1;33m-=-\033[m'*15)
print('ANALISADOR DE FINANCIAMENTO IMOBILIÁRIO')
print('\033[1;33m-=-\033[m'*15)
a = int(input('Digite o valor da casa:'))
b = int(input('Digite o salário atual:'))
c = int(input('Em quanto anos quer pagar?'))
c1 = c*12
a1 = a/c1
print('Para pagar uma casa de \033[35mR${:.2f}\033[m em \033[36m{}\033[m anos, a prestação mensal será de \033[35mR${:.2f}\033[m'.format(a, c, a1))
if a1 >= 1.3*b:
    print('Financiamento negado! Compromete demais a renda!')
else:
    print('Financiamento aprovado! Parabéns!')
