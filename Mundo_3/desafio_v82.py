# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.
numeros = list()
pares = list()
impares = list()

while True:
    numd = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N]? ').strip().upper()
    if numd not in numeros:
        numeros.append(numd)
    if numd % 2 != 0:
        impares.append(numd)
    else:
        pares.append(numd)
    if continuar == 'N':
        break
print('A lista completa é: ', numeros)
print('A lista de impares é: ', impares)
print('A lista de pares é: ', pares)
