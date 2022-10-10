# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

while True:
    num1 = int(input('Digite o 1.º valor: '))
    num2 = int(input('Digite o 2.º valor: '))
    oper = int(input('''# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Qual é a sua opção? '''))
    if oper == 1:
        print('O valor da soma é: {}'.format(num1 + num2))
    elif oper == 2:
        print('O valor da multiplicação é: {}'.format(num1 * num2))
    elif oper == 3:
        if num1 > num2:
            print('O maior número é: {}'.format(num1))
        elif num2 > num1:
            print('O maior número é {}'.format(num2))
    elif oper == 4:
        print('Tente novos valores: ')
    elif oper == 5:
        print('Saindo do programa...')
        sleep(2)
        print('Programa finalizado.')
        break
    else:
        print('Opção inválida, tente novamente!')
