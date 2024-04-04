def fatorial(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f


num = int(input('DIGITE UM VALOR: '))
fat = fatorial(num)
print(f'O FATORIAL DE {num} É {fat}')
