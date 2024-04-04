print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m    VALIDADOR DE ENTRADAS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = str(input('INFORME SEU SEXO: [M/F]').strip().upper()[0])
'''for x in range(1, 100):
    if a != 'M' and a!= 'F':
        a = str(input('DADO INVÁLIDO! INFORME SEU SEXO: [M/F]'))
    else:
        if a == 'M':
            print('SEU SEXO É MASCULINO. VAMOS PARA O PRÓXIMO PASSO!'.format(a))
        elif a == 'F':
            print('SEU SEXO É FEMININO. VAMOS PARA O PRÓXIMO PASSO!'.format(a))
        break'''
while a not in 'MF':
    a = str(input('DADO INVÁLIDO! INFORME SEU SEXO: [M/F]').strip().upper()[0])
if a == 'M':
    print('SEU SEXO É MASCULINO. VAMOS PARA O PRÓXIMO PASSO!'.format(a))
elif a == 'F':
    print('SEU SEXO É FEMININO. VAMOS PARA O PRÓXIMO PASSO!'.format(a))
