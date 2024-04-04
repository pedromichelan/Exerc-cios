a = {}
b = []
d = 0 #total de gols
a['NOME'] = str(input('NOME DO JOGADOR: '))
c = int(input(f'QUANTAS PARTIDAS {a["NOME"]} JOGOU?: '))
for x in range(0, c):
    b.append(int(input(f'QUANTO GOLS NA {x+1}º PARTIDA?: ')))
a['GOLS POR PARTIDA'] = b
for x in b:
    d += x
a['TOTAL'] = d
print('-=-'*12)
print(a)
print('-=-'*12)
for x, y in a.items():
    print(f'{x} = {y}')
print('-=-'*12)
print(f'O JOGADOR {a["NOME"]} JOGO {c} PARTIDAS')
for x in range(1, len(b)+1):
    print(f'=> NA PARTIDA {x}, FEZ {b[x-1]} GOLS')
