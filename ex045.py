from time import sleep
from random import choice

print('Bem-vindo ao Pedra Papel Tesoura!')
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jog = input('O que você escolhe? ').strip()


if jog == '1' or jog == '2' or jog == '3':
    sleep(0.5)
    print(f'{"JO" :^59}')
    sleep(0.5)
    print(f'{"KEN" :^60}')
    sleep(0.75)
    print(f'{"PO" :^59}')
    pc = choice(['Pedra', 'Papel', 'Tesoura'])
    lista = {'1': 'Pedra',
             '2': 'Papel',
             '3': 'Tesoura'}
    sleep(0.5)
    print('=-=' * 20)
    print(f'O \033[36mJogador\033[m escolheu ', end='')
    sleep(0.5)
    print(f'\033[36m{lista[jog]}\033[m')
    sleep(0.8)
    print(f'O \033[35mComputador\033[m escolheu ', end='')
    sleep(1.2)
    print(f'\033[35m{pc}\033[m')
    print('=-=' * 20)
    sleep(1)
    if lista[jog] == pc:
        print(f'\033[33;1m{"EMPATE" :^60}\033[m')
    elif lista[jog] == 'Papel' and pc == 'Pedra' or lista[jog] == 'Pedra' and pc == 'Tesoura' or lista[jog] == 'Tesoura' and pc == 'Papel':
        print(f'\033[1;32m{"JOGADOR VENCEU" :^60}\033[m')
    else:
        print(f'\033[1;31m{"COMPUTADOR VENCEU" :^60}\033[m')
else:
    print('Opção inválida. Tente novamente.')
