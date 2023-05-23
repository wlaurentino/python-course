# teste = list()
# teste.append('William')
# teste.append(35)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Alessandra'
# teste[1] = 32
# galera.append(teste[:])
# print(galera)

# galera = [['William', 35], ['Alessandra', 32], ['Rachel', 33], ['Maria', 72]]
# print(galera[0][0])

# galera = [['William', 35], ['Alessandra', 32], ['Rachel', 33], ['Maria', 72]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade')
