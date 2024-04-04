print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    DESCRIÇÃO DE UMA P.A. \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('PRIMEIRO TERMO: '))
b = int(input('RAZÃO DA P.A.: '))
c = 1
d = a
t = 0
n = 10
while n != 0:
    t = t + n
    while c <= t:
        print(d, end=' >> ')
        c = c + 1
        d = d + b
    print('PAUSA')
    n = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS?: '))
print('FORAM APRESENTADOS {} ITENS DA P.A.'.format(c-1))
print('FIM!')
