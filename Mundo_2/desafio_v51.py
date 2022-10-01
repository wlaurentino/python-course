# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA (Progressão Aritmética). No final, mostre os 10
# primeiros termos dessa progressão.

ptpa = int(input('Digite o Primeiro Termo da Progressão Aritmética: '))
razpa = int(input('Digite a razão da Progressão Aritmética: '))
for n in range(0, 10):
    print(ptpa + razpa * n, end=' ')
