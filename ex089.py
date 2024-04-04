print(f'{" ANÁLISE DE NOTAS DOS ALUNOS ":=^50}')
a = [] #final
b = [] #temporária
while True:
    b.append(str(input('NOME: ')))
    b.append(float(input('NOTA 1: ')))
    b. append(float(input('NOTA 2: ')))
    a.append(b[:])
    b.clear()
    c = str(input('DESEJA CONTINUAR? ').strip().upper()[0])
    if c == 'N':
        break
print('-=-'*15)
print(f'{"Nº":<7}{" NOME":<20}{"MÉDIA"}')
for i, x in enumerate(a):
    print(f'{i:<7}', f'{x[0]:<20}', f'{(x[1]+x[2])/2}')
print('-'*33)
while True:
    d = int(input('(999 INTERROMPE) - MOSTRAR NOTAS DO ALUNO (ÍNDICE): '))
    if d == 999:
        print('FINALIZANDO...')
        break
    else:
        for i, x in enumerate(a):
            if d == i:
                print(f'AS NOTAS DE {x[0]} SÃO {x[1]} E {x[2]}')
    print('-'*33)
