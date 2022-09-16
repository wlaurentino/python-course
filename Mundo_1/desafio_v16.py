# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela sua porção inteira
import math
nreal = float(input('Digite um número real:'))

print('O número real {} em inteiro é {}'.format(nreal, math.floor(nreal)))
