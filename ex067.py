print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m      TABUADAS DIVERSAS \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('QUER VER A TABUADA DE QUAL VALOR?: '))
print('---'*13)
while a > 0:
    for n in range(1, 11):
        print('{} X {} = {}'.format(a, n, a*n))
    print('---' * 13)
    a = int(input('QUER VER A TABUADA DE QUAL VALOR?: '))
    print('---'*13)
    if a < 0:
        break
print('ACABOU')
