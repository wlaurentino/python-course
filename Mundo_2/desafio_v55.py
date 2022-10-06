# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesop1 = float(input('Digite o 1.º peso: '))

contmaiorp = pesop1
contmenorp = pesop1


for c in range(2, 6):
    peso = float(input('Digite o {}.º peso: '.format(c)))
    if peso > contmaiorp:
        contmaiorp = peso
    elif peso < contmenorp:
        contmenorp = peso

print('O maior peso é {} e o menor é {}'.format(contmaiorp, contmenorp))
