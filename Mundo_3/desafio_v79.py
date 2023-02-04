# Crie um programa onde o usuário possa digitar vários valores números
# e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

numeros = list()

while True:
    numd = input('Digite um número: ')
    continuar = input('Quer continuar? [S/N]? ').strip().upper()
    if continuar == 'N':
        break
    if numd not in numeros:
        numeros.append(numd)
numeros.sort()
print(f'Os números digitados foram: {numeros}')
