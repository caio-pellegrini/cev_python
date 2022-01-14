import time

print('------ Calculadora para Pintores ------\n')
time.sleep(0.5)
nome = input('Você está precisando pintar uma parede, né? \nAntes de tudo, dê um nome a parede: ')
print(f'{nome}. Que nome legal! Agora sim, vamos ao que interessa.\n')
time.sleep(1)

lar = float(input(f'Qual a largura de {nome}? '))
alt = float(input(f'Qual a altura de {nome}? '))
time.sleep(1)
print('\nCerto! Já salvei os dados! Vou printar para você ver.')
time.sleep(0.7)

print(f'\n{nome} tem a dimensão de {lar :0.2f}m x {alt :0.2f}m.')
area = lar*alt
print(f'Isso significa que sua área é de {area :0.2f}m².\n')

time.sleep(1.5)
rende = float(input('Com 1 litro da tinta que você vai usar, dá pra pintar quantos m²? '))

print('OK, então vamos aos cáculos finais')
time.sleep(0.2)
print('Calculando...')
time.sleep(2)
print(f'Para pintar essa parede, você precisará de {area / rende :0.2f}l de tinta')
