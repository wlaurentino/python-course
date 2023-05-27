# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

num_estudantes = int(input("Digite o número de alunos: "))

for _ in range(num_estudantes):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    estudante = [nome, nota1, nota2]
    alunos.append(estudante)

print("Boletim:")
for estudante in alunos:
    nome = estudante[0]
    media = (estudante[1] + estudante[2]) / 2
    print(f"Aluno: {nome}   Média: {media:.2f}")

while True:
    nome = input("\nDigite o nome do aluno para ver as notas individuais (or 's' to sair): ")
    if nome.lower() == "s":
        break

    encontrado = False
    for estudante in alunos:
        if estudante[0] == nome:
            encontrado = True
            print(f"Notas para {nome}: {estudante[1]}, {estudante[2]}")
            break

    if not encontrado:
        print("Aluno não encontrado")
