# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionáriom
# em ordem, sabendo que o vencedor tirou o maior número no dado

import random
from time import sleep

resultados = {}

for jogador in range(1, 5):
    resultado = random.randint(1, 6)
    resultados[jogador] = resultado

resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1],
                              reverse=True)

print("Resultados dos jogadores:")
for jogador, resultado in resultados_ordenados:
    print(f"Jogador {jogador}: {resultado}")
    sleep(1)

vencedor = resultados_ordenados[0][0]
print(f"O vencedor é o Jogador {vencedor} com o maior número no dado!")
