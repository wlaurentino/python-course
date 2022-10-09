# Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random

numu = int(input('Descubra o número de 0 a 10 que o computador pensou: '))
numc = random.randrange(0, 10)
cont = 0

while numu != numc:
    numu = int(input('Errou !! Tente novamente: '))
    cont += 1

if numu == numc:
    print('Acertou !! Foram necessários {} palpites'.format(cont))
