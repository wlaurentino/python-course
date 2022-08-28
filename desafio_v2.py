# Crie um script Python que leia dois números
# e tente mostrar a soma entre eles.

num1 = int(input('Digite primeiro número da soma: '))
num2 = int(input('Digite segundo número da soma: '))
resultado = num1+num2

# print('A soma dos números é: ', resultado)
print('A soma vale {} '.format(resultado))
# print('A soma entra', num1, 'e', num2, 'é: ', resultado)
print('A soma entre {} e {} é {}'.format(num1, num2, resultado))
