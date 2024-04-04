print('='*30)
print('{:^30}'.format('NÚMEROS POR EXTENSO'))
print('='*30)
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    b = ' '
    while b not in range(0, 20):
        b = int(input('DIGITE UM NÚMERO ENTRE O E 20: '))
    print(f'VOCÊ DIGITOU O NÚMERO: {a[b]}')
    c = ' '
    while c not in 'SN':
        c = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
    if c == 'N':
        break
print('VOLTE SEMPRE!')
