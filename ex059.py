print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m     OPÇÕES COM NÚMEROS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('DIGITE O 1º NÚMERO: '))
b = int(input('DIGITE O 2º NÚMERO: '))
print('''OPÇÕES:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MOSTRAR O MAIOR
[ 4 ] DIGITAR NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
c = int(input('QUAL A SUA OPÇÃO?:'))
while c != 5:
    if c == 4:
        a = int(input('DIGITE O 1º NÚMERO: '))
        b = int(input('DIGITE O 2º NÚMERO: '))
        print('''OPÇÕES:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MOSTRAR O MAIOR
[ 4 ] DIGITAR NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
        c = int(input('QUAL A SUA OPÇÃO?:'))
    if c == 1:
        print('A SOMA ENTRE {} E {} É {}'.format(a, b, (a+b)))
        print('-------------')
        print('''OPÇÕES:
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MOSTRAR O MAIOR
        [ 4 ] DIGITAR NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA''')
        c = int(input('QUAL A SUA OPÇÃO?:'))
    if c == 2:
        print('A MULTIPLICAÇÃO ENTRE {} E {} É {}'.format(a, b, (a*b)))
        print('-------------')
        print('''OPÇÕES:
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MOSTRAR O MAIOR
        [ 4 ] DIGITAR NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA''')
        c = int(input('QUAL A SUA OPÇÃO?:'))
    if c == 3:
        if a > b:
            print('O MAIOR NÚMERO DIGITADO FOI {}'.format(a))
            print('-------------')
            print('''OPÇÕES:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MOSTRAR O MAIOR
            [ 4 ] DIGITAR NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA''')
            c = int(input('QUAL A SUA OPÇÃO?:'))
        elif b > a:
            print('O MAIOR NÚMERO DIGITADO FOI {}'.format(b))
            print('-------------')
            print('''OPÇÕES:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MOSTRAR O MAIOR
            [ 4 ] DIGITAR NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA''')
            c = int(input('QUAL A SUA OPÇÃO?:'))
        else:
            print('OS VALORES SÃO IGUAIS')
            print('-------------')
            print('''OPÇÕES:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MOSTRAR O MAIOR
            [ 4 ] DIGITAR NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA''')
            c = int(input('QUAL A SUA OPÇÃO?:'))
    if c < 1 or c > 5:
        c = int(input('OPÇÃO INVÁLIDA! TENTE NOVAMENTE: '))
print('FINALIZANDO ....')
from time import sleep
sleep(1)
print('ATÉ LOGO!')
