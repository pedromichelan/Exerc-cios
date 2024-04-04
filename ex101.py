def voto(a):
    from datetime import date
    a = int(input('EM QUE ANO VOCÊ NASCEU? '))
    b = date.today().year - a #idade
    c = ' '
    if b < 17:
        c = 'NÃO PROIBIDO'
    elif b == 17 or b > 70:
        c = 'VOTO OPCIONAL'
    else:
        c = 'VOTO OBRIGATÓRIO'
    print(f'COM {b} ANOS: {c}')


a = int(input(f'DIGITE SEU ANO DE NASCIMENTO: '))
voto(a)
