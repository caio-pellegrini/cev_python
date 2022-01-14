distancia = int(input('Qual a distância da sua viagem? '))
print(f'Se prepare, sua viagem de \033[1;36m{distancia}km\033[m está prestes a começar.')
bonus = 200
# a partir desse n de km, o passageiro ganha um desconto
if distancia <= 200:
    print(f'O preço da passagem será de \033[31mR${distancia * 0.50 :.2f}\033[m')
else:
    print(f'O preço da passagem será de \033[32mR${distancia * 0.45 :.2f}\033[m')
print(f'O preço da passagem será de \033[32mR${distancia * 0.50 if distancia <= 200 else distancia * 0.45 :.2f}')