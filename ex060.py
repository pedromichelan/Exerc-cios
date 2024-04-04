print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    FATORIAL DE UM NÚMERO \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('DIGITE UM NÚMERO PARA \nSABER SEU FATORIAL: '))
c = a
m = a
print('CALCULANDO {}! = '.format(a), end='')
while c >= 1:
    if c > 1:
        print('{}'.format(c), end=' X ')
        c = c -1
        m = m * c
    else:
        print('{}'.format(c), end='')
        c = c - 1
print(' = {}'.format(m))
