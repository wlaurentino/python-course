# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado
#  _  _  _
# 0|_||_||_|
# 1|_||_||_|
# 2|_||_||_|
# No final, mostre a matriz na tela, com a formatação correta.

numeros = [[], [], []]

for p in range(0, 3):
    for c in range(0, 3):
        numeros[p].append(int(input(f'Digite o valor para: [{p}, {c}] ')))
print('~*'*30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[{numeros[p][c]}]', end=' ')
print('')
