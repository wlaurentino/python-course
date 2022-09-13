# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ').strip())

while True:
    if 'SANTO' in cidade.upper():
        print('A cidade: {}, tem nome de SANTO'.format(cidade))
    else:
        print('A cidade: {}, não tem nome de SANTO'. format(cidade))
    break
