from random import randint
from time import sleep

print('=-' * 50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-' * 50)

num = randint(0, 5)
resp = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(randint(1, 4))

if resp == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'HAHAHA! Você errou! Eu pensei no número {num} e não no {resp}')