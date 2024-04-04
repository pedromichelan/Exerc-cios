print('\033[1;35m=\033[m'*25)
print('\033[1;36m       JO-QUEM-PÔ\033[m')
print('\033[1;35m=\033[m'*25)
from random import randint
a = randint(0,2)
print('''ESCOLHA UMA OPÇÃO:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
a1 = ['PEDRA', 'PAPEL', 'TESOURA']
b = int(input('QUAL SUA OPÇÃO?:'))
from time import sleep
sleep(.5)
print('JO')
sleep(.5)
print('QUEM')
sleep(.5)
print('PÔ')
sleep(.5)
print('OPÇÃO DO COMPUTADOR: {}'.format(a1[a]))
print('SUA OPÇÃO: {}'.format(a1[b]))
if a == b:
    print('JOGO EMPATADO!')
elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    print('O COMPUTADOR GANHOU!')
else:
    print('PARABÉNS! VOCÊ GANHOU!')


