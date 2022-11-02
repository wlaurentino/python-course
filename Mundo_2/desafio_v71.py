# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número int)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

vsaque = int(input('Qual será o valor sacado? R$ '))
totalsaq = vsaque
ced = 50
contced = 0
while True:
    if totalsaq >= ced:
        totalsaq -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if totalsaq == 0:
            break
