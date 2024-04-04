print(f'{" LISTAS PARES E ÍMPARES ":=^50}')
a = []
while True:
    c = int(input('DIGITE UM NÚMERO: (para parar "999")'))
    a.append(c)
    if c == 999:
        break
print(f'A LISTA COMPLETA É {a}')
d = [] #lista ímpares
e = [] #lista pares
for x in a:
    if x % 2 != 0:
        d.append(x)
    elif x % 2 == 0:
        e.append(x)
print(f'A LISTA DE ÍMPARES É {d}')
print(f'A LISTA DE ÍMPARES É {e}')
