print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m      ANÁLISE GRUPO PESOS \033[m')
print('\033[1;31;46m==\033[m'*20)
p1 = 0 #menor peso
p2 = 0 #maior peso
for x in range(1, 6):
    a = float(input('DIGITE O PESO DA {}ª PESSOA:'.format(x)))
    if x == 1:
        p1 = a
        p2 = a
    else:
        if a < p1:
            p1 = a
        elif a > p2:
            p2 = a
print('O MENOR PESO LIDO FOI {}'.format(p1))
print('O MAIOR PESO LIDO FOI {}'.format(p2))
