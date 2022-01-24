from time import sleep
from random import randint

print('Sou seu computador...')
sleep(1.5)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
numero = randint(0, 10)
sleep(1)
palpite = int(input('Qual é seu palpite? '))
c = 3
while c != 0 and palpite != numero:
    palpite = int(input(f'Errou! Você tem mais {c} chances: '))
    c -= 1
if c == 0:
    print(f'Game over! O número era {numero}')
else:
    print('Você acertou! PARABÉNS!')