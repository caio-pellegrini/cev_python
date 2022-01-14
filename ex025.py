nome = input('Qual é o seu nome completo? ').strip().lower().split()
# print(f'Seu nome contém Silva? {"silva" in nome}')
print(f'O seu nome {"contém" if "silva" in nome else "não contém"} a palavra "Silva"')