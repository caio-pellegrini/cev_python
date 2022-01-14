menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')