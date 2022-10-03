# Crie uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digie uma frase: ')).strip()

pali = frase.replace(' ', ',').upper()

print('O inverso da frase {} é {}'.format(frase, frase[::-1]))

if frase == frase[::-1]:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palíndromo')
