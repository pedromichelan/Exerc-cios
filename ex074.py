from random import randint
a = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'OS VALORES SORTEADOS FORAM: {a}')
'''b = a[0] #menor valor
c = a[0] #maior valor
for x in a:
    if x < b:
        b = x
    elif x > c:
        c = x
print(f'O MENOR VALOR SORTEADO FOI {b}')
print(f'O MAIOR VALOR SORTEADO FOI {c}')'''
print(f'O MENOR VALOR SORTEADO FOI {min(a)}')
print(f'O MAIOR VALOR SORTEADO FOI {max(a)}')
