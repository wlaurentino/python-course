# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas
# 2) O nome com todas as letras minúsculas
# 3) Quantas letras ao todo (sem considerar espaços)
# 4) Quantas letras tem o primeiro nome

nomec = str(input('Digite seu nome completo: '))
print('Seu nome em letras maiúsculas é: ', nomec.upper())
print('Seu nome em letras minúsculas é: ', nomec.lower())
print('Quantidade de letras no seu nome é: ', len(nomec) - nomec.count(' '))

nomep = nomec.split()

print('Quantidade de letras no seu primeiro nome é: ', len(nomep[0]))
