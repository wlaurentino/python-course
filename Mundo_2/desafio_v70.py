# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalc = contpmil = maisbarato = cont = 0
nomepbarato = ' '

while True:
    nomep = str(input('Digite o nome do produto: ')).strip()
    preçop = float(input('Digite o preço do produto: '))
    cont += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja sair do programa? - [S/N]: ')).strip().upper()
        [0]
    totalc += preçop
    if preçop > 1000:
        contpmil += 1
    if cont == 1 or preçop < maisbarato:
        maisbarato = preçop
        nomepbarato = nomep
    # else:
    #     if preçop < maisbarato:
    #         maisbarato = preçop
    #         nomepbarato = nomep
    if sair == 'S':
        print('Saindo do programa...')
        break
print(f'A) O total da compra é: {totalc}')
print(f'B) {contpmil} produtos custam mais de R$ 1000')
print(f'C) O produto mais barato foi: {nomepbarato} que custou {maisbarato}')
