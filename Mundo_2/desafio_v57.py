# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input('Digite o sexo - [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        print('O sexo da pessoa é {}'.format('Masculino'))
        break
    if sexo == 'F':
        print('O sexo da pessoa é {}'.format('Feminino'))
        break
    else:
        sexo != 'M' and 'F'
        print('Sexo inválido.')

# sexo = str(input('Digite o sexo - [M/F]: ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Sexo inválido, informe seu sexo: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso'.format(sexo))
