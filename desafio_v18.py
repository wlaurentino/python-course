# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
angulo = float(input('Digite o valor do ângulo: '))
radang = math.radians(angulo)

print("""O valor de seno é {:.2f}, o valor do cosseno é {:.2f} 
        e o valor da tangente é {:.2f}"""
      .format(math.cos(radang), math.sin(radang), math.tan(radang)))
