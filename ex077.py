print(f'{" ANALISADOR DE VOGAIS ":=^60}')
a = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
     'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
     'MERCADO', 'PROGRAMADOR', 'FUTURO')
b = ('A', 'E', 'I', 'O', 'U')
for x in range(0, len(a)):
    print(f'\nNA PALAVRA {a[x]} TEMOS: ', end='')
    for y in a[x]:
        if y in b:
            print(y, end=' ')
