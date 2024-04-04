def maior(*num):
    from time import sleep
    print('-=-'*13)
    print('ANALISANDO OS VALORES:')
    if num == ():
        print(f'FORAM INFORMADOS {len(num)} VALORES AO TODO.')
        print('NÃO EXISTE MAIOR VALOR.')
    else:
        for x in num:
            sleep(.3)
            print(x, end=' ', flush=True)
        print(f'\nFORAM INFORMADOS {len(num)} VALORES AO TODO.')
        print(f'O MAIOR VALOR INFORMADO FOI {max(num)}')


#PROGRAMA PRINCIPAL
maior(2, 5, 7, 8, 0, 6,33, 6000)
maior(4)
maior(-10, 200, 100000, 4)
maior()
