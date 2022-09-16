n1 = int(input('Um valor: '))
n2 = int(input('Outro valor:'))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
exp = n1 ** n2

print('A soma é {}, o produto é {}, e a divisão é {:.3f} '.format(soma, mult,
                                                                  div))
print('A divisão inteira é {} e a potência é {} '.format(divint, exp))
