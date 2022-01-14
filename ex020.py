import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]

# shuffle embaralha a lista
random.shuffle(lista)
print('A ordem de apresentação será:')
print(f'1° - {lista[0]}')
print(f'2° - {lista[1]}')
print(f'3° - {lista[2]}')
print(f'4° - {lista[3]}')

# sample apenas escolhe a quantidade de elementos passados no param. 2
print(random.sample(lista, 2))
