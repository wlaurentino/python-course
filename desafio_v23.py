# Faça um programa que leiam um número de 0 a 9999
# e mostre na tela cada um dos digítos separados.

num = int(input('Digite um número: '))
# "//" é a divisão inteira e "%" é o resto da divisão
print('A unidade do número é: ', num // 1 % 10)
print('A dezena do número é: ', num // 10 % 10)
print('A centena do número é: ', num // 100 % 10)
print('O milhar do número é: ', num // 1000 % 10)
