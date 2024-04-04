from random import randint
from time import sleep
print(f'{" ELABORADOR DE JOGOS MEGA SENA ":*^50}')
a = int(input('QUANTOS JOGOS VOCÊ QUER ELABORAR? '))
b = []
print('-='*4, f'ELABORANDO {a} JOGOS', '-='*4)
for y in range(0, a):
    for x in range(0, 7):
        b.append(randint(1, 61))
    sleep(1)
    print(f'JOGO {y+1}: {b}')
    b.clear()
