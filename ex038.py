print('\033[1;33m-=-\033[m'*8)
print('COMPARADOR DE NÚMEROS')
print('\033[1;33m-=-\033[m'*8)
a = float(input('DIGITE O PRIMEIRO NÚMERO: '))
b = float(input('DIGITE O SEGUNDO NÚMERO: '))
if a > b:
    print('O PRIMEIRO NÚMERO É MAIOR!')
elif b > a:
    print('O SEGUNDO VALOR É MAIOR!')
else:
    print('OS VALORES SÃO IGUAIS!')
