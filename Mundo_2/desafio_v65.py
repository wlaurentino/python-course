# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

cont = 0
soma = 0
maior = 0
menor = 0
sair = 'N'

while sair != 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma = num + num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sair = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print("""Você digitou {} números e a média entre eles foi {}
O maior valor foi {} e o menor foi {}"""
      .format(cont, soma/cont, maior, menor))
