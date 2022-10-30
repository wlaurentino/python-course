# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint

soma = 0
cont = 0

while True:
    num_usu = int(input('Digite um número de 1 a 10: '))
    num_pc = randint(0, 11)
    soma = num_usu + num_pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {num_usu} e o pc jogou {num_pc}, a soma foi {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu !!')
            cont += 1
        else:
            print('Você perdeu !!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você venceu !!')
            cont += 1
        else:
            print('Você perdeu !!')
            break
    print('Vamos jogar novamente...')
print(f'Fim de jogo!! Você venceu {cont} vezes!!')
