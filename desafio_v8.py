# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

metro = float(input('Digite o valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('O valor em quilômetros é: ', km)
print('O valor em hectômetros é: ', hm)
print('O valor em decâmetros é: ', dam)
print('O valor em decímetros é: ', dm)
print('O valor em centímetros é: ', cm)
print('O valor em milímetros é', mm)
