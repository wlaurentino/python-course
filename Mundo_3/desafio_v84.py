# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoa = list()
nomepeso = list()
lmaiorpeso = list()
lmenorpeso = list()

while True:
    nomepeso.append(str(input('Nome: ')))
    nomepeso.append(float(input('Peso: ')))
    pessoa.append(nomepeso[:])
    if len(pessoa) == 1:
        maior = menor = nomepeso[1]
    nomepeso.clear()
    while True:
        sair = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if sair in 'SN':
            break
    if sair == 'N':
        break

print('~*~'*30)
for p in pessoa:
    if p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]

for p in pessoa:
    if p[1] == maior:
        lmaiorpeso.append(p[0])
    elif p[1] == menor:
        lmenorpeso.append(p[0])

print(f'Ao todo, foram cadastradas {len(pessoa)} pessoas.')
print(f'O maior peso foi de {maior}, das pessoas {lmaiorpeso}')
print(f'O menor peso foi de {menor}, das pessoas {lmenorpeso}')
