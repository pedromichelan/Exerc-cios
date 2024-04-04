a = int(input('Digite um número de 0 a 9999:'))
u = a//1%10
d = a//10%10
c = a//100%10
m = a//1000%10
print('O número digitado foi {}'.format(a))
print('O número tem {} unidades'.format(u))
print('O número tem {} dezenas'.format(d))
print('O número tem {} centenas'.format(c))
print('O número tem {} mihares'.format(m))
