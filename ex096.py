def terreno():
    print('-'*30)
    print(f'{"CONTROLE DE TERRENO":^30}')
    print('-' * 30)
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    s = a * b
    print(f'A ÁREA DE UM TERRENO DE {a} X  {b} É DE {s}m²')


terreno()
terreno()
