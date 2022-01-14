from datetime import datetime

print('--- CLASSIFICANDO ATLETAS ---')
atual = datetime.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 0 or idade > 110:
    print('Ano inválido. Tente novamente')
else:
    print(f'O atleta tem {idade} anos.')
    if idade <= 9:
        print('Classificação: MIRIM')
    elif idade <= 14:
        print('Classificação: INFANTIL')
    elif idade <= 19:
        print('Classificação: JÚNIOR')
    elif idade <= 25:
        print('Classificação: SÊNIOR')
    else:
        print('Classificação: MASTER')
