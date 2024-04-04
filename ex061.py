print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    DESCRIÇÃO DE UMA P.A. \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('PRIMEIRO TERMO: '))
b = int(input('RAZÃO DA P.A.: '))
x = 1
while x in range(1, 10):
    if x == 1:
        print('{} -> '.format(a), end='')
        c = x * b
        print('{} -> '.format(a + c), end='')
        x += 1
    else:
        c = x * b
        print('{} -> '.format(a+c), end='')
        x += 1
print('FIM!')
