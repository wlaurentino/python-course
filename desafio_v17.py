# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo, calcule
# e mostre o comprimento da hipotenusa.
import math
catopost = float(input('Digite o cateto oposto: '))
catadjac = float(input('Digite o cateto adjacente: '))
comphipot = math.sqrt((catopost ** 2) + (catadjac ** 2))

print('O comprimento da hipotenusa é: {}'.format(math.floor(comphipot)))
