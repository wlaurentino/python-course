# Faça um programa em Python que abra e reproduza o áudio
# de um arquivo mp3

from pygame import mixer
import os

mixer.init()
mixer.music.load(os.path.join(os.path.dirname(__file__), 'desafio_v21.mp3'))
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Pression 'P' para pausar, 'V' para voltar")
    print("Pressione 'X' para fechar o programa")
    comando = input(" ")
    if comando in ('P', 'p'):
        mixer.music.pause()
    elif comando in ('V', 'v'):
        mixer.music.unpause()
    elif comando in ('X', 'x'):
        mixer.music.stop()
        break
