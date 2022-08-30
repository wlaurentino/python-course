# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido.

import random
dado = random.randint(0, 3)
print('Número sorteado: ', dado)
if dado == 0:
    print('Aluno número 0: Ale')
if dado == 1:
    print('Aluno número 1: Will')
if dado == 2:
    print('Aluno número 2: Dai')
if dado == 3:
    print('Aluno número 3: Thiagão')
