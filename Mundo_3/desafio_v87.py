# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

numeros = [[], [], []]

for p in range(0, 3):
    for c in range(0, 3):
        numeros[p].append(int(input(f'Digite o valor para: [{p}, {c}] ')))        
print('~*'*30)

# Printar a matriz
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[{numeros[p][c]}]', end=' ')
    print()

# Calcular a soma dos números pares
numero_par = 0
for p in range(0, 3):
    for c in range(0, 3):
        if numeros[p][c] % 2 == 0:
            numero_par += numeros[p][c]

# Calculando a soma da terceira coluna
soma_coluna = 0
for p in range(0, 3):
    soma_coluna += numeros[p][2]

# Maior valor da segunda linha
segunda_linha = numeros[1]
maior_valor = max(segunda_linha)

print(f"\nSoma dos números pares: {numero_par}")
print(f"Soma da terceira coluna: {soma_coluna}")
print(f"Maior valor da segunda linha: {maior_valor}")
