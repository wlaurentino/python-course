# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com a pausa de 1 segundo entre eles.

import time
import emoji
from pygame import mixer
import os

print('Contagem regressiva !!')
for cont in range(10, 0, -1):
    print(cont)
    time.sleep(1)
print(emoji.emojize(':fireworks:') * 10)
print('FELIZ ANO NOVO !!')
print(emoji.emojize(':fireworks:') * 10)

mixer.init()
mixer.music.load(os.path.join(os.path.dirname(__file__), 'desafio_v46.mp3'))
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Pressione 'X' para encerrar os fogos")
    comando = input(" ").upper()
    if comando == 'X':
        # Para o mixer
        mixer.music.stop()
        break
