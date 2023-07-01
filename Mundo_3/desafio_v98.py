# Faça um programa que tenha uma Função chamada contador(),
# que receba três parâmetros e mostre: ínicio, fim e passo
# e realizar a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

import time

def contador():
    print('Contagem De 1 até 10, de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
    print('\nContagem De 10 até 0, de 2 em 2')
    for d in range(10, -2, -2):
        print(d, end=' ')
    print('\nAgora é sua vez de personalizar a contagem')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    if passo == 0:
        print('Valor inválido para "Passo". O valor não pode ser zero.')
        return

    if inicio <= fim and passo < 0:
        print('Valor inválido para "Passo". O valor deve ser positivo ou zero para cancelar.')
        return

    if inicio >= fim and passo > 0:
        print('Valor inválido para "Passo". O valor deve ser negativo para fazer a contagem regressiva ou zero para cancelar.')
        return

    if inicio <= fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')


contador()

