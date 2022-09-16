# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para salário inferiores ou iguaiso, o aumente é de 15%

sal = float(input('Digite valor do seu salário: '))
aum1 = sal * 0.10
aum2 = sal * 0.15

if sal > 1.250:
    print('O seu novo salário é de {}'.format(sal + aum1))
else:
    print('O seu novo salário é {}'.format(sal + aum2))
