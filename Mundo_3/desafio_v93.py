# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou.
# Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA.
# No final, tudo isso será guardado em um DICIONÁRIO incluindo o TOTAL DE GOLS
# feitos durante o campeonato.

dicionario = {}
gols = []

dicionario['Nome'] = str(input('Digite o nome do jogador: '))
dicionario['Partidas'] = int(input(f'Quantas partidas jogou {dicionario["Nome"]}? '))

for c in range(dicionario['Partidas']):
    qgols = int(input(f'Quantos gols na partida {c}? '))
    gols.append(qgols)
    dicionario['Gols'] = gols
    dicionario['Total'] = sum(gols)

print('~*~'*10)
print(dicionario)
print('~*~'*10)
print('O nome do jogador é: ', dicionario['Nome'])
print('A quantidade de gols foram: ', gols)
print('O total de Gols foram: ', dicionario['Total'])
print('~*~'*10)
print(f'O jogador {dicionario["Nome"]} jogou {dicionario["Partidas"]} partidas')

for cont in range(dicionario['Partidas']):
    print('   => Na partida', cont, ' fez', gols[cont], ' gols')
