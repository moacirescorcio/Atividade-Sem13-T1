notas = []
for i in range(10):
    nota = int(input('Insira a nota do aluno(a): '))
    notas.append(nota)

print(f'Notas do aluno(a): {notas}')
print(f'Somatório das notas: {sum(notas)}')

produto = 1
for n in notas:
    produto = produto * n

print(f'Produto das notas: {produto}')