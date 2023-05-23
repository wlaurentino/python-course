# Crie um programa onde o usuário possa digitar sete valores números
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares
# em ordem crescente.

pares = list()
impares = list()

for p in range(0, 8):
    numeros = int(input('Digite o valor: '))
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(impares)}')
