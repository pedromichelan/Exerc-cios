def notas(*num, sit=False):
    """
    MOSTRA O TOTAL DE NOTAS APRESENTADAS, A MAIOR, A MENOR E A MÉDIA / SITUAÇÃO É OPCIONAL
    :param num: NOTAS APRESENTADAS, QUANTAS QUISER
    :param sit: SITUAÇÃO BOA (acima de 7) / REGULAR (entre 6 e 7) / RUIM (abaixo de 6)
    :return: DICIONÁRIO COM AS INFORMAÇÕES
    """
    s = 0
    for x in num:
        s += x
    m = s/len(num)
    if m < 6:
        aval = 'RUIM'
    elif 6<= m <= 7:
        aval = 'REGULAR'
    else:
        aval = 'BOA'
    if sit == False:
        b = {'TOTAL':len(num), 'MAIOR':max(num), 'MENOR':min(num), 'MÉDIA':m}
    if sit == True:
        b = {'TOTAL':len(num), 'MAIOR':max(num), 'MENOR':min(num), 'MÉDIA':m, 'SITUAÇÃO':aval}
    return b


#PROGRAMA PRINCIPAL
resp = notas(5.5, 8.5, 7.5, 8, 10, 1, sit=True)
help(notas)
print(resp)
