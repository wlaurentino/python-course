# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valorp = float(input('Digite o Valor do Produto: '))

while True:
    condp = int(input('''Digite o modo de pagamento
1 - à vista dinheiro ou cheque
2 - à vista no cartão
3 - em até 2x no cartão
4 - 3x ou mais no cartão
Qual será o modo de pagamento?

'''))
    if condp in [1, 2, 3, 4]:
        break
    else:
        # SE FOREM NÚMEROS DIFERENTES DE 1, 2 E 3
        print('Valor inválido !!')

if condp == 1:
    print('O valor do produto é {} e com desconto é {} : '
          .format(valorp, valorp - (valorp * 0.10)))
elif condp == 2:
    print('O valor do produto é {} e com desconto é {} : '
          .format(valorp, valorp - (valorp * 0.05)))
elif condp == 3:
    print('''Esse modo de pagamento não tem desconto,
o produto continua com o mesmo valor {}'''
          .format(valorp))
else:
    print('''O valor do produto é {} e com esse parcelamento o total é {},
pois há juros: '''
          .format(valorp, valorp + (valorp * 0.20)))
