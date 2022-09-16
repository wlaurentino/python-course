# Faça um programa que leia um ano qualquer
# e mostre se ele é BISSEXTO.

ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É um ano BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é um ano BISSEXTO'.format(ano))
