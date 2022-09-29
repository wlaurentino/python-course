# Refaça o desafio_v9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite o número: '))

for cont in range(1, 11):
    print('A tabuada de {} * {} = {}'.format(num, cont, (num * cont)))
