lista = []
for c in range(1, 6):
    lista.append(float(input(f'Peso da {c}º pessoa: ')))
print(f'O maior peso lido foi {max(lista)}kg')
print(f'O menor peso lido foi {min(lista)}kg')