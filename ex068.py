print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m      JOGO PAR OU ÍMPAR \033[m')
print('\033[1;31;46m==\033[m'*15)
from random import randint
d = 0
while True:
    a = int(input('DIGA UM VALOR: '))
    b = ' '
    while b not in 'PI':
        b = str(input('ESCOLHA PAR OU ÍMPAR [P/I]: ').strip().upper()[0])
    c = randint(0, 10)
    r = ''
    if (a+c) % 2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    print('VOCÊ JOGOU {} E O COMPUTADOR JOGOU {}. O TOTAL DEU {} QUE É {}'.format(a, c, a+c, r))
    if (a+c) % 2 == 0:
        if b == 'P':
            print('VOCÊ VENCEU!')
            d += 1
        else:
            print('VOCÊ PERDEU! FIM DE JOGO!')
            break
    else:
        if b == 'I':
            print('VOCÊ VENCEU!')
            d += 1
        else:
            print('VOCÊ PERDEU! FIM DE JOGO!')
            break
    print('VAMOS JOGAR NOVAMENTE!')
print('VOCÊ VENCEU {} VEZES!'.format(d))
