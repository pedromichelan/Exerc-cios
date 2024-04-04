print('\033[1;33m-=-\033[m'*15)
print('CONVERSOR DE BASES NUMÉRICAS')
print('\033[1;33m-=-\033[m'*15)
a = int(input('Digite um número inteiro:'))
print('Escolha uma das bases de conversão')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter par OCTAL
[ 3 ] converter para HEXADECIMAL
''')
b = int(input('Digite sua opção:'))
if b == 1:
        print('O número {} em BINÁRIO se escreve {}'.format(a, bin(a)))
if b == 2:
    print('O número {} em OCTAL se escreve {}'.format(a, oct(a)))
if b == 3:
    print('O número {} em HEXADECIMAL se escreve {}'.format(a, hex(a)))
if b !=1 and b!=2 and b!=3:
    print('Opção inválida!!!')
