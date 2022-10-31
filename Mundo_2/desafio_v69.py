# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idade = contmaior = conth = contm = 0
sexo = ' '
sair = ' '

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo - [M/F]: ')).strip().upper()[0]
    sair = str(input('Quer continuar o programa? - [S/N]: ')).strip().upper()
    [0]
    if idade > 18:
        contmaior += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1
    if sair == 'N':
        print('Finalizando programa...')
        break
print(f'A) {contmaior} pessoas maiores de idade foram cadastradas')
print(f'B) {conth} homens foram cadastrados')
print(f'C) {contm} mulheres menores de 20 anos foram cadastradas')
