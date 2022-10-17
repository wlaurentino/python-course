# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).

cont = 0
num = 0
soma = 0

while num != 999:
    num = int(input('Digite o número: '))
    if num != 999:
        soma = soma + num
        cont += 1
print('Foram somados {} número e sua soma é: {}'.format(cont, soma))
