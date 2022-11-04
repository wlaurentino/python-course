# Crie um programa que tenha uma TUPLA totalmente preenchida
# com uma contagem por extenso, de Zero até Vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

numext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
          'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número de 0 a 20: '))
while num not in range(0, 20):
    num = int(input('Número inválido! Digite um número de 0 a 20: '))
print(f'O número digitado foi: {numext[num]}')
