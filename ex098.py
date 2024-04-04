def contador(i, f, p):
    from time import sleep
    print('-=-'*12)
    if p < 0:
        print(f'CONTAGEM DE {i} A {f} DE {-p} EM {-p}')
    else:
        print(f'CONTAGEM DE {i} A {f} DE {p} EM {p}')
    if i < f:
        for x in range(i, f+1, p):
            print(f'{x}', end=' ')
            sleep(.3)
        print('FIM!')
    else:
        if p > 0:
            p *= -1
        for x in range(i, f-1, p):
            print(f'{x}', end=' ')
            sleep(.3)
        print('FIM!')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, -2)
print('-=-'*12)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM')
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
contador(i, f, p)
