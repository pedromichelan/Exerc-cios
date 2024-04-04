def leiaInt(a):
    while True:
        try:
            b = int(input(a))
            return b
            break
        except(ValueError, TypeError):
            print('\33[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\33[m')
        except(KeyboardInterrupt):
            print('\33[31mO USUÁRIO PREFERIU NÃO DIGITAR ESSE VALOR!\33[m')
            return 0

def linha(a=40):
    return '-' * a

def cabecalho(txt, a=35):
    print(linha(a))
    print(txt.center(a))
    print(linha(a))

def menu(lista, txt, a):
    cabecalho(txt, a)
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print(linha(a))
    opc = leiaInt('\33[32mDIGITE SUA OPÇÃO: \33[m')
    return opc

