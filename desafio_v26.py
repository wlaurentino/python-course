# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').upper()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela 1.ª vez na posição {} '
      .format(frase.find('A')))
print('A letra "A" aparece pela última vez na posição {}'
      .format(frase.rfind('A')))
