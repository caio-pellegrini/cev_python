from random import randint

print('Acabei de pensar em um número de 0 a 10. Tente adivinhar...')
num = randint(1, 10)
palpite = int(input('Seu palpite: '))
c = 0
while palpite != num:
    if palpite > num:
        dica = 'menor'
    elif palpite < num:
        dica = 'maior'
    palpite = int(input(f'O valor é {dica}. Tente novamente: '))
    c += 1
print(f'Acertou!! Você precisou de {c} {"tentativa" if c == 1 else "tentativas"}')