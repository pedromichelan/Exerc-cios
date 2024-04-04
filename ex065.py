print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    INFORMAÇÕES DE NÚMEROS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = b = x = 0
c = 'S'
while c == 'S':
    x = int(input('DIGITE UM NÚMERO: '))
    a += 1
    b += x
    if a <= 1:
        m1 = x  # maior valor
        m2 = x  # menor valor
    else:
        if x > m1:
            m1 = x
        elif x < m2:
            m2 = x
    c = str(input('DESEJA CONTINUAR? [S/N]: ').upper().strip()[0])
print('VOCÊ DIGITOU {} NÚMEROS E A MÉDIA FOI {}'.format(a, b/a))
print('O MAIOR NÚMERO DIGITADO FOI {} E O MENOR FOI {}'.format(m1, m2))
