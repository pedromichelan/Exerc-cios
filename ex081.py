a = []
while True:
    b = int(input('DIGITE UM VALOR: '))
    a.append(b)
    c = ' '
    while c not in 'SN':
        c = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
    else:
        if c == 'N':
            break
print(f'VOCÊ DIGITOU {len(a)} ELEMENTOS!')
#a.sort(reverse=True)
d = sorted(a, reverse=True)
print(f'OS VALORES EM ORDEM DECRECENTE SÃO {d}')
if 5 in a:
    print('O VALOR 5 FAZ PARTE DE LISTA!')
else:
        print('O VALOR 5 NÃO FAZ PARTE DA LISTA!')
print(a)
