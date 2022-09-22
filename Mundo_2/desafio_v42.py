# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

reta1 = int(input('Digite o lado 1 do triângulo: '))
reta2 = int(input('Digite o lado 2 do triângulo: '))
reta3 = int(input('Digite o lado 3 do triângulo: '))

if (reta2 - reta3) < reta1 < reta2 + reta3:
    if (reta1 - reta3) < reta2 < reta1 + reta3:
        if (reta1 - reta2) < reta3 < reta1 + reta2:
            print('As retas FORMAM um triângulo')
            if reta1 == reta2 == reta3:
                print('Essas retas formam um triângulo EQUILÁTERO')
            elif reta1 != reta2 != reta3:
                print('Essas retas formam um triângulo ESCALENO')
            else:
                print('Essas retas formam um triângulo ISÓSCELES')
else:
    print('As retas NÃO formam um triângulo')
