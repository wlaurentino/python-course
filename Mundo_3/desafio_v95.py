# Aprimore o desafio 93 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema
# de visualização de DETALHES DE APROVEITAMENTO de cada jogador.

jogadores = []

while True:
    dicionario = {}
    gols = []

    dicionario['Nome'] = str(input('Digite o nome do jogador: '))
    dicionario['Partidas'] = int(input(f'Quantas partidas {dicionario["Nome"]} jogou? '))

    for c in range(dicionario['Partidas']):
        qgols = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(qgols)

    dicionario['Gols'] = gols
    dicionario['Total'] = sum(gols)

    jogadores.append(dicionario)

    continuar = input('Deseja cadastrar outro jogador? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('~' * 30)
print('Cod', 'Nome', 'Gols por Partida', 'Total de Gols')
print('-' * 60)

for i, jogador in enumerate(jogadores):
    gols_por_partida = ' '.join(str(gols) for gols in jogador['Gols'])
    print('{:<5} {:<15} {:<15} {:<15}'.format(i+1, jogador['Nome'], gols_por_partida, jogador['Total']))

print('-' * 60)

while True:
    detalhes = int(input('Mostrar detalhes de qual jogador? (Digite código do jogador ou 0 para sair): '))

    if detalhes == 0:
        break

    if detalhes > len(jogadores):
        print('Jogador não encontrado!')
    else:
        jogador = jogadores[detalhes - 1]
        print(f'\nAproveitamento do jogador {jogador["Nome"]}:')
        for partida, gols in enumerate(jogador['Gols']):
            print(f'   => Na partida {partida+1} fez {gols} gol(s)')

print('Fim do programa')

