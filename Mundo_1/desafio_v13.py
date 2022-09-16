# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

sfunc = float(input('Digite o valor do salário: '))
aument = (sfunc * 15/100) + sfunc

print('O novo salário do funcionário é: ', aument)
