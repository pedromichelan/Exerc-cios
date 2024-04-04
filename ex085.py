print(f'{" EXTRAINDO LISTA DE OUTRA LISTA ":^^60}')
a = [[ ], [ ]] #principal
b = 0
for x in range(1, 8):
    b = int(input(f'DIGITE O {x}º VALOR: '))
    if  b % 2 == 0:
        a[0].append(b)
    else:
        a[1].append(b)
print(f'OS VALORES PARES DIGITADOS FORAM: {a[0]}')
print(f'OS VALORES ÍMPARES DIGITADOS FORAM: {a[1]}')
