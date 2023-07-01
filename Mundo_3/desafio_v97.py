# Faça um programa que tenha uma Função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável
# Ex: escreva('Olá Mundo!')
# ~~~~~~~~~~~
# Olá Mundo!
# ~~~~~~~~~~~
def escreva(texto):
    print(texto)
    print('~*' * len(texto))


escreva('Olá Mundo!')
escreva('Quero aprender a Desenvolver')
escreva('Espero conseguir um dia')
escreva('Se Deus quiser')
