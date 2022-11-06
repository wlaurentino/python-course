# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3?
# C) Quais foram os números pares?

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um valor: '))
num4 = int(input('Digite o último número: '))
ntupla = num1, num2, num3, num4

print(f'Você digitou os valores {ntupla}')
print(f'O valor 9 apareceu {ntupla.count(9)} vez(es)')
if 3 in ntupla:
    print(f'O valor 3 apareceu na {ntupla.index(3, 1)+1}.ª posição ')
else:
    print('O valor 3 não apareceu em NENHUMA posição')
print('Os valores pares digitados foram: ')
for npartup in ntupla:
    if(npartup % 2 == 0):
        print(npartup)
