# Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de 3 e
# que se encontram no íntervalo de 1 até 500.

# c de contador

vrept = 0
for c in range(1, 500):
    imp = c % 2
    mult3 = c % 3
    if imp == 1 and mult3 == 0:
        vrept += c
print('A soma dos números entre 1 e 500 é: {}'.format(vrept))
