# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada

import random
a1 = input('Digite o nome do 1.º aluno: ')
a2 = input('Digite o nome do 2.º aluno: ')
a3 = input('Digite o nome do 3.º aluno: ')
a4 = input('Digite o nome do 4.º aluno: ')

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print("""A ordem do sorteio foi {}"""
      .format(lista))
