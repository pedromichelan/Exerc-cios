from random import randint
from time import sleep
from operator import itemgetter
a = {}
b = []
for x in range(1, 5):
    a[f'JOGADOR {x}'] = randint(1,6)
print('VALORES SORTEADOS: ')
for x, y in a.items():
    print(f'O {x} TIROU: {y}')
    sleep(1)
b = sorted(a.items(), key=itemgetter(1), reverse=True)
print('-=-'*15)
print(f'{" RANKING DOS JOGADORES ":*^30}')
for x, y in enumerate(b):
    print(f'{x+1}º LUGAR: {y[0]} COM {y[1]}')
