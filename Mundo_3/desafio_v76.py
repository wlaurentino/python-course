# Crie um programa que tenha uma Tupla única com
# nomes de produtos e seus respectivos preços na sequência
# No final, mostre uma listagem de preços, organizando os dados
# em forma tabular.

listupla = ('Café', 21.12, 'Creatina', 50, 'Whey Protein', 80)
print('~'*30)
print('{:^30}' .format('LISTAGEM DE PREÇOS'))
print('~'*30)
for n in range(0, len(listupla)):
    if n % 2 == 0:
        print('{:.<30}R${:>7.2f}'.format(listupla[n], listupla[n+1]))
print('~'*30)
