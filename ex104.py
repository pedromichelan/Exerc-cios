def leiaInt(a):
    b = input(a)
    while b.isnumeric() == False:
        print(f'\33[31m{"ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO."}\33[m')
        b = input(a)
    return b


#PROGRAMA PRINCIAL
n = leiaInt('DIGITE UM NÚMERO INTEIRO: ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {n}.')
