print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
quantidade = int(input('Quantos termos você quer mostrar? '))
atual = 0
ultimo = 0
penultimo = 0
while quantidade > 0:
    if quantidade >= 2 and atual == 0:
        print(f'0 → 1 → ', end='')
        ultimo = 1
        atual = 1
        quantidade -= 2
    else:
        atual = ultimo + penultimo
        print(f'{atual} → ', end='')
        penultimo = ultimo
        ultimo = atual
        quantidade -= 1
print('\033[31mFIM\033[m')