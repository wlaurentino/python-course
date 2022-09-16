# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

vcarro = int(input('Digite a velocidade do carro: '))
vmulta = (vcarro - 80) * 7
if vcarro <= 80:
    print('Velocidade {} está dentro do limite'.format(vcarro))
else:
    print('O valor da multa é: ', vmulta)
