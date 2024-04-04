a = {}
b = []
d = []
while True:
    b.clear()
    a.clear()
    a['NOME'] = str(input('NOME DO JOGADOR: '))
    c = int(input(f'QUANTAS PARTIDAS {a["NOME"]} JOGOU?: '))
    for x in range(0, c):
        b.append(int(input(f'QUANTO GOLS NA {x+1}º PARTIDA?: ')))
    a['GOLS POR PARTIDA'] = b[:]
    a['TOTAL'] = sum(b)
    d.append(a.copy())
    while True:
        e = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
        if e not in 'SN':
            print('ERRO! DIGITE S OU N!')
        else:
            break
    if e == 'N':
        break
print('-=-'*12)
print(f'{"COD":^4}', f'{"NOME":<15}', f'{"GOLS/PARTIDA":<20}', f'{"TOTAL":<7}')
for x, y in enumerate(d):
    print(f'{x:^4}', f'{y["NOME"]:<15}', f'{str(y["GOLS POR PARTIDA"]):<20}', f'{y["TOTAL"]:<7}')
while True:
    f = (int(input('MOSTRAR DADOS DE QUAL JOGADOR? (999 PARA PARAR): ')))
    if f == 999:
        print('FIM!')
        break
    else:
        if f not in range(0, len(d)):
            print(f'NÃO EXISTE JOGADOR COM O CÓDIGO {f}')
        else:
            print(f'- LEVANTAMENTO DO JOGADOR: {d[f]["NOME"]}')
            k = 1
            for x in d[f]['GOLS POR PARTIDA']:
                print(f'NO JOGO {k} FEZ {x} GOLS.')
                k += 1
