print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m     ANALISADOR DE NÚMEROS PRIMOS \033[m')
print('\033[1;31;46m==\033[m'*20)
a = int(input('DIGITE UM NÚMERO: '))
b = range(1, a+1, 1)
c = 0
for x in b:
    if a % x == 0:
        print('\033[34m', end=' ')
        c = c + 1
    else:
        print('\033[32m', end=' ')
    print(x, end=' ')
if c <= 2:
    print('O NÚMERO {} É PRIMO!'.format(a))
else:
    print('NÃO É PRIMO!')
print('ACABOU!')
