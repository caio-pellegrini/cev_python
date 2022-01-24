sexo = input('Digite seu sexo: [M/F] ').upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = input('Valor inválido. Digite seu sexo novamente [M/F] ').strip().upper()
print(f'Entendi, seu sexo é {sexo}')