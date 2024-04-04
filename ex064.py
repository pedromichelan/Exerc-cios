print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    SOMA DE NÚMEROS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = b = x = 0
x = int(input('DIGITE UM NÚMERO [999 PARA PARAR]: '))
while x != 999:
    b = b + x
    a = a + 1
    x = int(input('DIGITE UM NÚMERO [999 PARA PARAR]: '))
print('VOCÊ DIGITOU {} NÚMEROS E A SOMA ENTRE ELES FOI {}'.format(a, b))
