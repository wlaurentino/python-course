# Crie um programa que faça o computador jogar Jokenpô com você.

import emoji
from random import randint

while True:
    jogadapc = randint(0, 2)

    while True:
        suajogada = int(input(emoji.emojize('''Digite sua jogada
0 - Pedra :oncoming_fist:
1 - Papel :hand_with_fingers_splayed:
2 - Tesoura :victory_hand:

''')))
        if suajogada in [0, 1, 2]:
            break
        else:
            # SE FOREM NÚMEROS DIFERENTES DE 1, 2 E 3
            print('Valor inválido !!')

    if suajogada == 0 and jogadapc == 2:
        print(emoji.emojize('''Você VENCEU !!
Sua jogada foi Pedra :oncoming_fist:
e a do computador foi Tesoura :victory_hand:'''))
        break
    elif suajogada == 1 and jogadapc == 0:
        print(emoji.emojize('''Você VENCEU !!
Sua jogada foi Papel :hand_with_fingers_splayed:
e a do computador foi Pedra :oncoming_fist:'''))
        break
    elif suajogada == 2 and jogadapc == 1:
        print(emoji.emojize('''Você GANHOU !!
Sua jogada foi Tesoura :victory_hand:
e a do computador foi Papel :hand_with_fingers_splayed:'''))
        break
    elif suajogada == jogadapc:
        print('EMPATE !! Jogue novamente')
    else:
        print(emoji.emojize('Você perdeu !! :sad_but_relieved_face:'))
        break
