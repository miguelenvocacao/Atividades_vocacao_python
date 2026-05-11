# Anuario do aluno(a)

nome = input("Digite seu nome completo: ")
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
serie = input("Digite sua série atual: ")
materias_notas = {}

for i in range(1, 4):
    materia = input(f"Digite a matéria {i}: ")
    nota = float(input(f"Digite a nota de {materia}: "))
    materias_notas[materia] = nota  

idade = 2026 - int(data_nascimento.split("/")[2])

print(f"\n=== ANUÁRIO DO ALUNO(A) ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Série: {serie}")
print(f"Notas: {materias_notas}")