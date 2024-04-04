def sorteio():
    from random import randint
    a = []
    x = 0
    while x <= 4:
        a.append(randint(-100, 100))
        x += 1
    print(f'SORTEANDO 5 VALORES DA LISTA: ',*a, f'PRONTO!')
    b = 0
    for y in a:
        if y % 2 == 0:
            b += y
    print(f'SOMANDO OS VALORES PARES DE {a}, TEMOS: {b}')

sorteio()
