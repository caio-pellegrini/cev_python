from datetime import date
menor_idade = 0
maior_idade = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if atual - ano >= 18:
        maior_idade += 1
    elif atual - ano < 18:
        menor_idade += 1
print(f'Existem {menor_idade} pessoas menores de idade, e {maior_idade} maiores de idade')