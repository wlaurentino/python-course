# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nomeC = input('Digite o nome completo: ').title()

nomeP = nomeC.split(' ', 1)[0]
nomeU = nomeC.rsplit(' ', 1)[-1]

print('O primeiro nome é: ', nomeP)
print('O último nome é: ', nomeU)
