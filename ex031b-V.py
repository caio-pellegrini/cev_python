distancia = int(input('Qual a distância da sua viagem? '))
print(f'Se prepare, sua viagem de \033[1;36m{distancia}km\033[m está prestes a começar.')
bonus = 200
# a partir desse n de km, o passageiro ganha um desconto
if distancia <= bonus:
    passagem = 0.55
    preco = distancia * passagem
    print(f'O preço da passagem será de \033[31mR${preco :.2f}\033[m')
else:
    passagem = 0.45
    preco = distancia * passagem
    print(f'O preço da passagem será de \033[32mR${preco :.2f}')