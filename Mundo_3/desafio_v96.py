# Faça um programa que tenha uma Função chamada area(),
# que receba as dimensões de um Terreno retangular
# (Largura e Comprimento) e mostre a Área do Terreno



def area(largura, comprimento):
    a = 0
    a = largura * comprimento
    print(f'A área do terro é {largura}x{comprimento} é de {a}m²')


# Programa Principal
print('Controle de Terrenos')
print('~*'*30)

area(float(input('Insira a Largura em metros: ')),
     float(input('Insira o Comprimento em metros: ')))
