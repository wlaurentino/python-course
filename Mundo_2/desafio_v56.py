# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# ~> A média de idade do grupo.
# ~> Qual é o nome do homem mais velho.
# ~> Quantas mulheres têm menos de 20 anos.

idadesoma = 0
maior_idade = 0
nomemv = 0
mulhermenor20 = 0

for cont in range(1, 5):
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idadesoma += idade
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nomev = nome
    elif sexo == 'F' and idade < 20:
        mulhermenor20 += 1

print('A média de idade do grupo é: {:.1f}'.format(idadesoma / 4))
print('O homem mais velho do grupo é: {}'.format(nomev))
print('Há {} mulhere(s) com menos de 20 anos de idade'.format(mulhermenor20))
