def fatorial(a=1, show=False):
    """
    RETORNA O FATORIAL DO NÚMERO EM QUESTÃO
    :param a: NÚMERO
    :param show: MOSTRAR A CONTA PADRÃO False
    :return: O FATORIAL
    """
    b = 1
    c = a
    if show == False:
        for x in range(a, 0, -1):
            b *= x
        return b
    if show == True:
        for x in range(a, 1, -1):
            print(f' {c} ', end='x')
            b *= x
            c -= 1
        print(f' {c} = ', end='')
    return b


print(fatorial(6, True))
