# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o 1.º número: '))
num2 = int(input('Digite o 2.º número: '))
num3 = int(input('Digite o 3.º número: '))

# Verificando quem é o Menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o Maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O Menor número digitado foi: {} '.format(menor))
print('O Maior número digitado foi: {} '.format(maior))
