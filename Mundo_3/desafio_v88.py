# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntas quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

import random

num_jogos = int(input("Quantos jogos você quer gerar "))
palpites_megasena = []

for i in range(num_jogos):
    palpite = random.sample(range(1, 61), 6)
    palpites_megasena.append(palpite)

print("Sorteando:")
for i, palpite in enumerate(palpites_megasena, 1):
    print(f"Jogo {i}: {palpite}")
