# Crie uma TUPLA preenchida com os 20 primeiros colocado da Tabela
# do CAMPEONATO BRASILEIRO DE FUTEBOL de 2022, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians',
         'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Fortaleza', 'Botafogo',
         'América-MG', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'Avaí', 'Chapecoense')

print(f'A) Os 5 primeiro colocados são: {times[0:5]}')
print(f'B) Os 4 últimos colocados são: {times[16:]}')
print(f'C) Times em ordem alfabética {sorted(times)}')
print('D) O time da Chapecoense está na posição: ',
      times.index('Chapecoense')+1)
