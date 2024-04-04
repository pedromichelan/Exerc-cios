print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    SOMA DE NÚMEROS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = b = x = 0
while True:
    x = int(input('DIGITE UM NÚMERO [999 PARA PARAR]: '))
    if x == 999:
        break
    b = b + x
    a = a + 1
print('VOCÊ DIGITOU {} NÚMEROS E A SOMA ENTRE ELES FOI {}'.format(a, b))
