print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m   OS 10 PRIMEIROS TERMOS DE UMA P.A. \033[m')
print('\033[1;31;46m==\033[m'*20)
a = int(input('DIGITE O PRIMEIRO TERMO DA P.A.: '))
b = int(input('DIGITE A RAZÃO DA P.A.: '))
c = range(1, 11)
'''for x in c:
    print(a, end='->')
    a = a + b
print('ACABOU!!')'''
d = range(a, a+(b*10), b)
for x in d:
    print(x, end=' -> ')
print('ACABOU2!')
