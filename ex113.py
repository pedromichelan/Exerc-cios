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

def leiaFloat(a):
    while True:
        try:
            b = float(input(a))
            return b
            break
        except (ValueError, TypeError):
            print('\33[31mERRO! DIGITE UM NÚMERO REAL VÁLIDO!\33[m')
        except(KeyboardInterrupt):
            print('\33[31mO USUÁRIO PREFERIU NÃO DIGITAR ESSE VALOR!\33[m')
            return 0



#PROGRAMA PRINCIAL
n = leiaInt('DIGITE UM NÚMERO INTEIRO: ')
r = leiaFloat('DIGITE UM NÚMERO REAL: ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO INTEIRO {n} E O NÚMERO REAL {r}.')
