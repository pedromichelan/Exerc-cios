print('\033[1;35m=\033[m'*25)
print('\033[1;36m   PROGRAMA DA TABUADA \033[m')
print('\033[1;35m=\033[m'*25)
a = int(input('DIGITE O NUMERO PARA VER SUA TABUADA: '))
b = range(1, 11)
for x in b:
    print('{} X {} = {}'.format(a, x, a*x))
