# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
anonasc = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year

if ano - anonasc <= 9:
    print('O atleta tem {} anos e sua categora é MIRIM'
          .format(ano - anonasc))
elif (ano - anonasc) > 9 and (ano - anonasc) <= 14:
    print('O atleta tem {} anos e sua categora é INFANTIL'
          .format(ano - anonasc))
elif (ano - anonasc) > 14 and (ano - anonasc) <= 19:
    print('O atleta tem {} anos e sua categora é JÚNIOR'
          .format(ano - anonasc))
elif (ano - anonasc) > 19 and (ano - anonasc) <= 25:
    print('O atleta tem {} anos e sua categora é SÊNIOR'
          .format(ano - anonasc))
else:
    (ano - anonasc) > 25
    print('O atleta tem {} anos e sua categoria é MASTER'
          .format(ano - anonasc))
