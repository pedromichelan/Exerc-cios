print('\033[1;33m-=-\033[m'*15)
print('    ANALISADOR DE AUMENTO SALARIAL')
print('\033[1;33m-=-\033[m'*15)
a = float(input('Digite o salário do funcionário em questão:'))
b = 1.15
c = 1.10
print('A salário atual é de \033[1;35mR${:.2f}\033[m'.format(a))
if a <= 1250:
    print('O salário reajustado será: \033[1;33mR${:.2f}\033[m'.format(a*b))
if a > 1250:
    print('O salário reajustado será: \033[1;33mR${:.2f}\033[m'.format(a*c))
