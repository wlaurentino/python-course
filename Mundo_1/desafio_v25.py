# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

nomep = str(input('Digite o nome da pessoa: ').strip())

while True:
    if 'SILVA' in nomep:
        print('A pessoa: {}, tem SILVA no nome'.format(nomep.upper()))
    else:
        print('A pessoa: {}, não tem SILVA nome'. format(nomep.upper()))
    break
