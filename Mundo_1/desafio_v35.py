# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = int(input('Digite o lado 1 do triângulo: '))
reta2 = int(input('Digite o lado 2 do triângulo: '))
reta3 = int(input('Digite o lado 3 do triângulo: '))

if (reta2 - reta3) < reta1 < reta2 + reta3:
    if (reta1 - reta3) < reta2 < reta1 + reta3:
        if (reta1 - reta2) < reta3 < reta1 + reta2:
            print('As retas FORMAM um triângulo')

else:
    print('As retas NÃO formam um triângulo')
