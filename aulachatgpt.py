''' # Função para separar números em pares e ímpares
def separar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

# Solicitar números ao usuário
entrada = input("Digite números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Separar os números em pares e ímpares
pares, impares = separar_pares_impares(numeros)

# Mostrar os resultados
print("Números pares:", pares)
print("Números ímpares:", impares)'''


'''entrada = input('Digite um número separado por espaços')
print(type(entrada))
b = list(map(int, entrada.split()))
print(type(b))
print(b)'''

entrada = '1 2 3 4 5'
b = list(map(int, entrada.split()))
print(type(b))
print(b)
