# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()

while True:
    numd = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N]? ').strip().upper()
    if continuar == 'N':
        break
    if numd not in numeros:
        numeros.append(numd)
print('A) Foram digitados: ', len(numeros), 'números')
numeros.sort(reverse=True)
print('B) A lista de valores ordenadas de forma decrescente é:', numeros)
if 5 in numeros:
    print('C) O número 5 está na lista')
else:
    print('C) O número 5 não está na lista')
