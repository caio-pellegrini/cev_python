from time import sleep

times = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América MG', 'Atlético GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Atlético PR', 'Cuiabé',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

# TABELA COMPLETA

print('TABELA BRASILEIRÃO')
sleep(1)
for posicao, time in enumerate(times):
    posicao += 1
    print(f'{posicao}º - {time}')
sleep(1)
print('---------')
sleep(1)

# CINCO PRIMEIROS COLOCADOS

print('Os cinco primeiros colocados:')
sleep(1)
for posicao, time in enumerate(times[:5]):
    posicao += 1
    print(f'{posicao}º - {time}')
sleep(1)
print('---------')
sleep(1)

# QUATRO ÚLTIMOS COLOCADOS

print('Os quatro úlitmos colocados:')
sleep(1)
for posicao, time in enumerate(times[-4:]):
    posicao += 17
    print(f'{posicao}° - {time}')
sleep(1)
print('---------')
sleep(1)

# TIMES EM ORDEM ALFABÉTICA

print('Times em ordem alfabética:')
sleep(1)
for time in sorted(times):
    print(time)
sleep(1)
print('---------')
sleep(1)

# POSIÇÃO DA CHAPECOENSE

pos_chapeco = times.index("Chapecoense") + 1
print(f'A Chapecoense está na {pos_chapeco}° posição')