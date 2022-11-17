# Crie um programa que tenha uma tupla
# com várias palavras (SEM ACENTOS).
# Depois disos, você deve mostrar,
# para cada palavras, quais são as vogais.

palavtupla = ('estudar', 'trabalhar', 'programar', 'viajar',
              'aproveitar', 'curtir', 'etcetera')

for p in palavtupla:
    print(f'\n Na palavra {p.upper()} as vogais são: ', end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
