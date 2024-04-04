print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m  ESTATÍSTICAS GRUPO DE PESSOAS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = b = c = 0
# a = total pessoas maiores / b = total homens / c = total mulheres menor de 20 anos
while True:
    print('-'*15)
    print('CADASTRE UMA PESSOA')
    print('-' * 15)
    i = int(input('IDADE: '))
    s = ' '
    while s not in 'MF':
        s = str(input('SEXO [M/F]: ').strip().upper()[0])
    t = ' '
    while t not in 'SN':
        t = str(input('QUER CONTINUAR? [S/N]: ').strip().upper()[0])
    if i > 18:
        a += 1
    if s == 'M':
        b += 1
    if s == 'F' and i < 20:
        c += 1
    if t == 'N':
        break
print('TOTAL PESSOAS COM MAIS DE 18 ANOS: {}'.format(a))
print('TOTAL PESSOAS DO SEXO MASCULINO: {}'.format(b))
print('TOTAL MULHERES COM MENOS DE 20 ANOS: {}'.format(b))
