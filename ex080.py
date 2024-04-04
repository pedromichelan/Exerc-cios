print(f'{" ORGANIZADOR DE LISTAS ":x^50}')
a = []
for x in range(0, 5):
    b = int(input('DIGITE UM VALOR: '))
    if x == 0 or b > a[-1]:
        a.append(b)
        print('O VALOR FOI PARA O FINAL!')
    else:
        y = 0
        while y < len(a):
            if b <= a[y]:
                a.insert(y, b)
                print(f'O VALOR FOI PARA A POSIÇÃO {y}')
                break
            y += 1
print(f'OS VALORES FORAM: {a}')
