# Faça um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário
# venceu ou perdeu

import random
from pygame import mixer
import os

numc = random.randrange(0, 5)
numu = int(input('Descubra o número de 0 a 5 que o computador pensou: '))

if numu == numc:
    print('ASERTO Miserávi !! O número do computador é {}, e o seu é {}'
          .format(numc, numu))

    mixer.init()
    mixer.music.load(os.path.join(os.path.dirname(__file__),
                     'desafio_v28_a.mp3'))
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        print("Pressione 'X' para encerrar a sonoplastia")
        comando = input(" ").upper()
        if comando == 'X':
            mixer.music.stop()
            break
else:
    print('ERRROU !! O número do computador é {}, e o seu é {}'
          .format(numc, numu))
    mixer.init()
    mixer.music.load(os.path.join(os.path.dirname(__file__),
                     'desafio_v28_e.mp3'))
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        print("Pressione 'X' para encerrar a sonoplastia")
        comando = input(" ").upper()
        if comando == 'X':
            mixer.music.stop()
            break
