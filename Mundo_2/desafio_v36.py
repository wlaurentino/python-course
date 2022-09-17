# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

vcasa = float(input('Digite o valor da casa/ap: '))
salario = float(input('Digite o seu salário: '))
anop = float(input('Em quantos anos será o parcelamento? '))

if vcasa / (12 * anop) > (salario * 0.30):
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado !!')
