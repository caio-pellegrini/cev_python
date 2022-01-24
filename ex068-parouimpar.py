from random import randint

print('=-' * 20)
print('Vamos jogar par ou ímpar!')
vitorias = 0


# def numero para verificar se o numero é valido


def escolha_jogador():
    while True:
        try:
            escolha = input('Par ou Ímpar? ').strip().upper().replace('I', 'Í')[0]
            if escolha in 'PÍ':
                break
        except IndexError:
            pass
        print('Valor inválido, tente novamente')
    return escolha


while True:
    print('=-' * 20)
    jogador = int(input('Digite um valor: '))
    escolha = escolha_jogador()
    print('-' * 40)
    computador = randint(0, 10)
    soma = jogador + computador
    # se o resultado for True, é par, se for False, é ímpar
    parouimpar = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print(f'JOGADOR: {jogador} - COMPUTADOR: {computador} - TOTAL: {soma}')
    if parouimpar[0] == escolha:
        print(f'\033[32mDEU {parouimpar} - Você venceu!\033[m')
        vitorias += 1
        print('Vamos jogar novamente...')
    else:
        print(f'\033[31mDEU {parouimpar} - Você perdeu!\033[m')
        break
print('=-' * 20)
print(f'GAME OVER! Você me derrotou {vitorias} {"vez" if vitorias == 1 else "vezes"}')
