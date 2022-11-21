# Faça um programa que leia 5 valores númericos
# e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições
# na lista

maior = 0
menor = 0
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'O maior valor digitado é: {max(valores)} nas posições... ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}...', end='')
print(f'O menor valor digitado é: {min(valores)} nas posições... ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}...', end='')
