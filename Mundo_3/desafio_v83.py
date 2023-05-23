# Crie um programa em Python onde o usuário digite uma expressão matemática
# que use parênteses.  O aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta

lista = []
expressao = input('Digite uma expressão: ').strip()

for carac in expressao:
    if carac == '(':
        lista.append('(')
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
