# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
# ~~ NÚMEROS PRIMOS SÃO AQUELES DIVISÍVEIS POR 1 E POR ELE MESMO ~~

num = int(input('Digite um número: '))
contnp = 0
for n in range(1, num+1):
    if num % n == 0:
        contnp += 1
if contnp == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))
    print(contnp)
