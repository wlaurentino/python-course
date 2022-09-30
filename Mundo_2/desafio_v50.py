# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

vrept = 0
for cont in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        vrept += num
    else:
        print('O valor digitado é ímpar e não será considerado na soma')
print(vrept)
