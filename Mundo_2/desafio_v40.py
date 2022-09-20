# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a 1.ª nota: '))
n2 = float(input('Digite a 2.º nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Aluno REPROVADO, a média foi {}. Você deveria se dedicar mais'
          .format(media))
elif media >= 5.0 and media <= 6.9:
    print('''Aluno em RECUPERAÇÃO, a média foi {}.
            Prepara-se para a próxima prova'''
          .format(media))
else:
    print('Aluno APROVADO !! A média foi {}. Parabéns !!'
          .format(media))
