# Escreva um programa que leia dois números inteiros e compare-os.
# Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite o 1.º número: '))
num2 = int(input('Digite o 2.º número: '))

if num1 > num2:
    print('O número {} é MAIOR que o número {}'
          .format(num1, num2))
elif num2 > num1:
    print('O número {} é MAIOR que o número {}'
          .format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais.')
