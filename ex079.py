print(f'{"FORMADOR DE LISTA":-^50}')
a = []
while True:
    b = int(input('DIGITE UM VALOR: '))
    if b not in a:
        a.append(b)
        print('VALOR ADICIONADO COM SUCESSO!')
    else:
        print('VALOR DUPLICADO! NÃO ADICIONADO!')
    c = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
    if c == 'N':
        break
print('OS VALORES DIGITADOS FORAM {}'.format(sorted(a)))
