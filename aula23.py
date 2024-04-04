try:
    a = int(input('NUMERADOR: '))
    b = int(input('DENOMINADOR: '))
    r = a/b
except Exception as erro:
    print(f'HOUVE UM ERRO DO TIPO {erro.__class__}')
else:
    print(f'O RESULTADO É {r}')
finally:
    print('VOLTE SEMPRE!')
