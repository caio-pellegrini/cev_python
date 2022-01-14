from time import sleep
from random import random, choice

velocidade = random()
maximo = choice([80, 90, 100, 110])
print('====== RADAR FIXO ======')
print(f'Preste atenção!')
sleep(0.2)
print(f'O limite dessa rodovia é de {maximo}km/h')
sleep(1)
print('')
for a in range(10):
    print('🚗', end=" ")
    sleep(1 - velocidade)
sleep(1)
print('\nVocê acabou de passar pelo radar!')
print('')
sleep(1)
print('Calculando velocidade...')
sleep(2)
velocidade_int = int(velocidade*140)
print(f'Você passou a {velocidade_int}km/h')
if velocidade_int > maximo:
    print('Ah não! Você ultrapassou o limite de velocidade')
    print(f'Por conta disso, você será multado em R${(velocidade_int - maximo) * 9 :.2f}')
    sleep(3)
    print('Placa do veículo registrada e multa já debitada')
    print('Diriga com segurança e tenha uma ótima viagdem!')
else:
    print('Você está dentro do limite de velocidade! Tenha uma boa viagem e continue pagando impostos!')
