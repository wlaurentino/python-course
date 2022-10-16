# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Digite a quantidade de número da Sequência de Fibonacci: '))
n1 = 0
n2 = 1
soma = 0
count = 1

while count <= n:
    n1 = n2
    n2 = soma
    soma = n1 + n2
    count += 1
    print('{} ~> '.format(soma), end='')
