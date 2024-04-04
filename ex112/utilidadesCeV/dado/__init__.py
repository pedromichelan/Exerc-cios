def leiaDinheiro(msg):
    while True:
        x = str(input(msg))
        if x.isnumeric():
            return float(x)
            break
        elif '.' in x:
            x1 = float(x)
            return x1
            break
        elif ',' in x:
            x1 = float(x.replace(',', '.'))
            return x1
            break
        else:
            print('ERRO! DIGITE UM PREÇO VÁLIDO.')
