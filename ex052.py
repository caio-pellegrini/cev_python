print('\nSerá que esse número é primo?')
num = int(input('Digite um número: '))
divisivel = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        divisivel += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisível {divisivel} vezes')
if divisivel == 2:
    print('Por isso ele \033[34mÉ PRIMO\033[m')
else:
    print('Por isso ele \033[36mNÃO É PRIMO\033[m')
