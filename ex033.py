print('\033[1;33m-=-\033[m'*10)
print('    ANALISADOR DE NÚMEROS')
print('\033[1;33m-=-\033[m'*10)
a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))
if a < b and a < c:
    print('O menor valor digitado foi: {}!'.format(a))
if b < a and b < c:
    print('O menor valor digitado foi: {}!'.format(b))
if c < a and c < b:
    print('O menor valor digitado foi: {}!'.format(c))
if a > b and a > c:
    print('O maior valor digitado foi: {}!'.format(a))
if b > a and b > c:
    print('O maior valor digitado foi: {}!'.format(b))
if c > a and c > b:
    print('O maior valor digitado foi: {}!'.format(c))
if a == b == c:
    print('Os três números são iguais!')
