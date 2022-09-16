# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

dado = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(dado))
print('Só tem espaços? ', dado.isspace())
print('É um número? ', dado.isnumeric())
print('É alfabético', dado.isalpha())
print('É alfa númerico? ', dado.isalnum())
print('Está toda em maiúsculas? ', dado.isupper())
print('Está toda em minúsculas? ', dado.islower())
print('Esta capitalizada - 1.ª letra maiúsculas', dado.istitle())
