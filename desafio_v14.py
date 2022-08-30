# Escreva um programa que converta uma temperatura digitada em °C
# e converta para °F

celsius = float(input('Digite a temperatura em °C: '))
fahrenheit = 9 * celsius / 5 + 32

print('A tempera {} °C em {} °F é: '.format(celsius, fahrenheit))
