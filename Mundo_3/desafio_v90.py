# Faça um programa que leia NOME e MÉDIA de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo na tela

situacao = {'Situacao1': 'Aprovado', 'Situacao2': 'Reprovado'}
nome_aluno = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))
if media >= 7:
    print(situacao['Situacao1'])
else:
    print(situacao['Situacao2'])
