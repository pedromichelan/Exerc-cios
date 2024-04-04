print('\033[1;35m=\033[m'*32)
print('\033[1;36m   SOMADOR DE 6 NÚMEROS PARES \033[m')
print('\033[1;35m=\033[m'*32)
a = range(1, 7)
soma = 0
for x in a:
    num = int(input('DIGITE O {}° NÚMERO: '.format(x)))
    if num % 2 == 0:
        soma = soma + num
print(soma)
