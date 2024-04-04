print('\033[1;33m-=-\033[m'*10)
print('   ANALISADOR DE TRIÂNGULOS')
print('\033[1;33m-=-\033[m'*10)
print('\033[32mVamos analisar se os segmentos apresentados podem formar um triângulo\033[m')
a = float(input('Segmento 01:'))
b = float(input('Segmento 02:'))
c = float(input('Segmento 03:'))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos apresentados podem formar um triângulo!')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
