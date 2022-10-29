# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

num = 0
cont = 0

while True:
    num = int(input('De qual número deseja ver a tabuada? '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'A tabuada de {num} * {cont} = {num * cont}')
print('Programa de tabuada finalizado.')
