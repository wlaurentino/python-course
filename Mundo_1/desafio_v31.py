# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200KM
# e R$0,45 para viagens mais longas.

dviagem = float(input('Digite a distância da viagem em KM: '))
viagemc = dviagem*0.50
viageml = dviagem*0.45
if dviagem <= 200:
    print('O valor da passagem até 200KM é: {:.2f}'.format(viagemc))
else:
    print('O valor da passagem além 200KM é: {:.2f}'.format(viageml))
