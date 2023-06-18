# Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO
# e cadastre-os (com IDADE) em um dicionário se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO.
# Calcule e acrescente, além da IDADE, com quantos anos e pessoa vai ser APOSENTAR.

dicionario = {}

while True:
    dicionario['Nome'] = str(input('Digite o nome: '))
    dicionario['Ano Nascimento'] = int(input('Digite o ano de nascimento: '))
    dicionario['CTPS'] = int(input('Digite a CTPS (0 não tem): '))
    if dicionario['CTPS'] == 0:
        print('Não tem CTPS')
        break
    if dicionario['CTPS'] != 0:
        dicionario['Idade'] = 2023 - dicionario['Ano Nascimento']
    dicionario['Ano contratação'] = int(input('Digite o ano de contratação: '))
    dicionario['Salário'] = str(input('Digite o salário: '))
    dicionario['Aposentadoria'] = (dicionario['Ano contratação'] + 35) - dicionario['Ano Nascimento']
    sair = input("Aperte S para sair: ").upper()
    if sair == 'S':
        break
print('Nome: ', dicionario['Nome'])
print('Idade: ', dicionario['Idade'])
print('CTPS: ', dicionario['CTPS'])
print('Ano contratação: ', dicionario['Ano contratação'])
print('Salário: € ', dicionario['Salário'])
print('Aposentadoria: ', dicionario['Aposentadoria'], ' anos')
