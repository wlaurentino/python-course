# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

brl = float(input('Digite o valor em Reais: '))
usd = brl / 4.96

print('É possível comprar {:.2f} dólares'.format(usd))
