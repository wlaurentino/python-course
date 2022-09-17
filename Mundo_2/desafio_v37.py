# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
tconv = 0
num = int(input('Digite um número inteiro: '))

while True:
    tconv = int(input('Digite o tipo de conversão 1-bin, 2-oct, 3-hex: '))
    nbin = bin(num)
    noct = oct(num)
    nhex = hex(num)
    if tconv in [1, 2, 3]:
        break
    else:
        # SE NÃO FOREM NÚMEROS DIFERENTES DE 1, 2 E 3
        print('Valor inválido !!')

if tconv == 1:
    print('O número {} convertido em binário é: {}'
          .format(num, nbin[2:]))
elif tconv == 2:
    print('O número {} convertido em octal é: {}'
          .format(num, noct[2:]))
elif tconv == 3:
    print('O número {} convertido em hexadecial é: {}'
          .format(num, nhex[2:]))
