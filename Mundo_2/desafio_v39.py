# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou
# se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date
anonasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year

if (ano - anonasc) < 18:
    print('AINDA FALTAM {} ano(s) para você se alistar'
          .format(18 - (ano - anonasc)))
elif (ano - anonasc) > 18:
    print('''O QUE VOCÊ ESTÁ ESPERANDO?! Você deveria ter se alistado há {} ano(s)
    e você NÃO se alistou'''.format((ano - anonasc) - 18))
else:
    (ano - anonasc) == 18
    print('PARABÉNS!! Você tem {} anos é sua vez de servir o Brasil'
          .format(ano - anonasc))
