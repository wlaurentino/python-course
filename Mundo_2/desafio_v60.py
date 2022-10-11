# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# import math

# num = int(input('Digite um número: '))

# print('O fatorial de {} é {}'.format(num, math.factorial(num)))

fat = 1
n = 1
numdig = int(input('Digite o número: '))

while n <= numdig:
    fat *= n
    n += 1
print('O fatorial do número é: {}'.format(fat))
