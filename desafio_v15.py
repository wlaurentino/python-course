# Escreva um programa que pergunte a quantidade de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 650 por dia
# e R$ 0,15 por KM rodado

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pag = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pag))
