# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ').upper())

while True:
    if 'SANTO' and 'SÃO' in cidade:
        print('A cidade: {}, tem nome de SANTO'.format(cidade))
    else:
        print('A cidade: {}, não tem nome de SANTO'. format(cidade))
    break
