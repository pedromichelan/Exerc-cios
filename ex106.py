def PyHELP():
    while True:
        from time import sleep
        print('\33[46m~'*23)
        print('SISTEMA DE AJUDA PyHELP')
        print('~' * 23)
        print('\33[m')
        a = str(input('FUNÇÃO OU BIBLIOTECA (FIM p/ FINALIZAR)> '))
        print('\33[47m~' * 23)
        print(f'ACESSANDO MANUAL DE {a}')
        print('~' * 23)
        print('\33[m')
        sleep(2)
        print('\33[42m')
        print(help(a))
        print('\33[4m')
        if a.upper() == 'FIM':
            break


PyHELP()
