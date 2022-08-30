# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.asin(angulo)

print('O valor de seno é {}'.format(seno))
