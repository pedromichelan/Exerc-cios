print('='*30)
print('{:^30}'.format('NÚMEROS POR EXTENSO'))
print('='*30)
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        b = int(input('DIGITE UM NÚMERO: '))
        if 0 <= b <= 20:
            break
    print('VOCÊ DIGITOU O NÚMERO {}'.format(a[b]))
    while True:
        c = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
        if c in 'SN':
            break
    if c == 'N':
        break
print('VOLTE SEMPRE!')
