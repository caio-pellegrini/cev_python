num = int(input('Digite um valor para ver seu fatorial: '))
print(f'{num}! = {num}', end='')
total = num
for c in range(num-1, 0, -1):
    print(f' x {c}', end='')
    total *= c
print(f' = {total}')

# ------- // -------

from math import factorial
num = int(input('Digite um número para ver seu fatorial: '))
print(f'O fatorial de {num} é {factorial(num)}')
