print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m       JOGO ADIVINHAÇÃO \033[m')
print('\033[1;31;46m==\033[m'*15)
print('''OLÁ SOU SEU COMPUTADOR!
ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 A 10.
SERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL FOI?''')
from random import randint
a = randint(0, 10)
b = int(input('QUAL É O SEU PALPITE?: '))
c = 1
while b != a:
    c = c + 1
    if b < 0 or b > 10:
        b = int(input('PALPITE INVÁLIDO! TENTE OUTRA VEZ!: '))
    else:
        if b < a:
            b = int(input('MAIS.... TENTE OUTRA VEZ!: '))
        if b > a:
            b = int(input('MENOS.... TENTE OUTRA VEZ! '))
print('PARABÉNS VOCÊ ACERTOU COM {} TENTATIVAS! EU ESCOLHI O NÚMERO {}!'.format(c, a))
'''c = 0
x = 1
while x < 10:
    c = c + 1
    x = int(input('DIGITE UM NÚMERO:'))
print(c)'''
