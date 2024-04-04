a = [['Pedro', 20], ['Maria', 18], ['João', 30]]
print(a[0][0])
a = []
g = []
a.append('PEDRO')
a.append(37)
g.append(a[:])
a[0] = 'MARIA'
a[1] = 25
g.append(a[:])
print(g)
l = [['CADEIRA', 44], ['TV', 1000], ['ESTANTE', 600], ['CANETA', 3]]
print(l[0][1])
