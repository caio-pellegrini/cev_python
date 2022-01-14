import random

print('------------- EMBARALHADOR DE LISTAS - SORTEIO ALUNOS -------------')
qnt = int(input('Quantos alunos irão apresentar? '))
lista = []

for a in range(1, qnt + 1):
    lista.append(input(f'Digite o nome do(a) {a}° aluno(a): '))

random.shuffle(lista)

print('\nA ordem de apresentação será:')
for a in range(len(lista)):
    print(f'{a + 1}° aluno: {lista[a]}')