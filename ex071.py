print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m         BANCO MICHELAN \033[m')
print('\033[1;31;46m==\033[m'*15)
a = int(input('QUAL VALOR VOCÊ QUER SACAR: R$'))
b = 0  #cont 50
c = 0  #cont 20
d = 0  #cont 10
e = 0  #cont 1
f = 0  #resto
while True:
    if a >= 50:
        a -= 50
        b += 1
    else:
        if a >= 20:
            a -= 20
            c += 1
        else:
            if a >= 10:
                a -= 10
                d += 1
            else:
                if a > 0:
                    a -= 1
                    e += 1
                else:
                    break
if b > 0:
    print(f'TOTAL DE {b} CÉDULAS DE R$50,00')
if c > 0:
    print(f'TOTAL DE {c} CÉDULAS DE R$20,00')
if d > 0:
    print(f'TOTAL DE {d} CÉDULAS DE R$10,00')
if e > 0:
    print(f'TOTAL DE {e} CÉDULAS DE R$10,00')
