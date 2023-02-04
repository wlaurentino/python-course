# Crie um programa onde o usuário possa digitar cinco valores númericos
# e cadastre-os em uma lista, já na posição correta de inserção.
# No final, mostre a lista ordenada na tela (sem usar o sort()).

valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
valores.sort()
print(valores)
