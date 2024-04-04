from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado
#n = int(input('DIGITE O VALOR: R$'))
n = dado.leiaDinheiro('DIGITE O PREÇO: R$')
print(n)
moeda.resumo(n, 150, 30)
