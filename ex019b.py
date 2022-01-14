import random
import time

time.sleep(0.5)
print('\n----------- SORTEIO DE ALUNOS -----------')
time.sleep(0.5)
qnt = int(input('Quantos alunos estarão participando? '))
lista_a = []
print('')

for a in range(1, qnt + 1):
    lista_a.append(input(f'Digite o nome do(a) {a}° aluno(a): '))

print('\nOkay, todos os nossos foram adicionados!')
print('O sorteio irá começar...')
time.sleep(1.5)
print('\nSorteando...')
time.sleep(3.5)
sor = random.choice(lista_a)
print(f'\nO aluno(a) sorteado foi o(a) {sor}!!')
print(f'Processo finalizado com sucesso.\n{sor} foi sorteado dentre {qnt} participantes')