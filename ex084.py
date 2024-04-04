print(f'{" NOME E PESO ":-^50}')
a = [] #final
b = [] #local
d = 0 #contador pessoas
e = [] #lista de pesos
while True:
    b.append(str(input('NOME: ')))
    b.append(float(input('PESO: ')))
    a.append(b[:])
    b.clear()
    d += 1
    c = str(input(('DESEJA CONTINUAR? [S/N]: ')).strip().upper()[0])
    if c == 'N':
        break
print(f'AO TODO CADASTROU {d} PESSOAS')
for x in range(0, len(a)):
    e.append(a[x][1])
print(f'O MAIOR PESO FOI {max(e)}KG PESO DE ', end='')
for y in range(0, len(a)):
    if a[y][1] == max(e):
        print(a[y][0], end=' ')
print(f'\nO MENOR PESO FOI {min(e)}KG PESO DE ', end='')
for z in range(0, len(a)):
    if a[z][1] == min(e):
        print(a[z][0], end=' ')
