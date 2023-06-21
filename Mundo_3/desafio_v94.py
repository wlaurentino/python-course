# Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa
# em um DICIONÁRIO e todos os dicionários em uma LISTA. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A MÉDIA de idade do grupo.
# C) Uma lista com todas as MULHERES
# D) Uma lista com todas as pessoas com IDADE acima da MÉDIA

dicionario = {}
lista = []
mulheres = []
idades = []
acimamedia = []
contar = 0
media = 0

while True:
    dicionario = {}
    dicionario['Nome'] = str(input('Nome: '))
    lista.append(dicionario['Nome'])

    chaveconta = "Nome"
    for nome in dicionario:
        if nome == chaveconta:
            contar += 1

    dicionario['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    lista.append(dicionario['Sexo'])
    if dicionario['Sexo'] == 'F':
        mulheres.append(dicionario['Nome'])

    dicionario['Idade'] = int(input('Idade: '))
    lista.append(dicionario['Idade'])
    idades.append(dicionario['Idade'])

    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

media = sum(idades) / len(idades)

for contidade in idades:
    if contidade > media:
        index = idades.index(contidade)
        acimamedia.append(lista[index * 3])

print(lista)
print('A) Quantidade de pessoas cadastradas:', contar)
print('B) A MÉDIA de idade do grupo é:', media)
print('C) Lista de mulheres:', mulheres)
print('D) Pessoas com IDADE acima da MÉDIA:')
for nome in acimamedia:
    print(nome)
