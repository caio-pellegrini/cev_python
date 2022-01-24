"""from time import sleep
from random import randint

print('Sou seu computador...')
sleep(1.5)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
numero = randint(0, 10)
sleep(1)
palpite = int(input('Qual é seu palpite? '))
while palpite != numero:
    palpite = int(input('Errou! Tente novamente: '))
print('Acertou!')"""

# do jeito que tava na aula
from random import randint
computador = randint(0, 10)
palpites = 0
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print(f'Acertou com {palpites} tentativas. Parabéns')
