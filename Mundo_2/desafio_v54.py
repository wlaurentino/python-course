# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date

ano = date.today().year
contmenor18 = 0
contmaior18 = 0

for c in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento: '))
    if ano - anonasc < 18:
        contmenor18 += 1
    elif ano - anonasc >= 18:
        contmaior18 += 1
print('Há {} menores de 18 anos e {} maiores de 18'
      .format(contmenor18, contmaior18))
