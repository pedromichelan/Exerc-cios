'''a = ['a', 'b', 'c']
a.sort(reverse=True)
print('os valores são: ')
for i, x in enumerate(a):
    print(f'posição {i}    valor {x}')
b = [1, 2, 3, 9, 5]
b[0] = 9
b.append(10)
b.insert(1, 44)
b.sort(reverse=True)
b.pop(4)
b.remove(3)
while True:
    if 9 in b:
        b.remove(9)
    else:
        print('Nao tem mais 9!')
        break
del(b[3])
print(b)
print(f'ESSA LISTA TEM {len(b)} ELEMENTOS.')'''
a = []
for x in range(0, 5):
    a.append(int(input('DIGITE UM VALOR: ')))
print(a)
b = a[:]
print(b)
a.append(b)
print(f'A LISTA {a} EXTENDIDADE')
