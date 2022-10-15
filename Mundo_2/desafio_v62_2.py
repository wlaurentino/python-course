# Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da Prograssão Aritmética: '))
razão = int(input('Digite a Razão Aritmética: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ~> '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
