# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

pprod = float(input('Digite o preço do produto: '))
vdesc = pprod - (pprod * 5/100)

print('Preço com desconto é {:.2f}'.format(vdesc))
