# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valores
# que estão na tupla.

from random import randint

vso = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)

valor_max = max(vso)
valor_min = min(vso)

print(f'Os número gerados foram: {vso}')
print(f'O maior valor na tupla é {valor_max}')
print(f'O menor valor na tupla é {valor_min}')
