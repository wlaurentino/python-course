# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro termo da Prograssão Aritmética: '))
razão = int(input('Digite a Razão Aritmética: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} ~> '.format(termo), end=' ')
    termo += razão
    cont += 1
