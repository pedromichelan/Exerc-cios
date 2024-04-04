print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    SEQUÊNCIA DE FIBONACCI \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR?: '))
b = 0
c = 1
d = 0
e = 1
if a == 1:
    print('{} >>'.format(b), end='')
elif a == 2:
    print('{} >> '.format(b), end='')
    print('{} >>'.format(c), end='')
else:
    print('{} >> '.format(b), end='')
    print('{} >>'.format(c), end='')
    while e <= a-2:
        d = b + c
        print(' {} >>'.format(d), end='')
        b = c
        c = d
        e = e +1
print(' FIM!')
