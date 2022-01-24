maiores = homem = mulher_menor_20 = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA:" :^30}')
    print('-' * 30)

    # idade
    idade = int(input('Idade: '))

    # sexo
    while True:
        try:
            sexo = input('Sexo: [M/F] ').strip().upper()[0]
            if sexo in 'MF':
                break
        except IndexError:
            pass
        print('Valor inválido. Tente novamente')

    # analise de dados
    if idade > 18:
        maiores += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1

    print('-' * 30)
    while True:
        try:
            continua = input('Quer continuar? [S/N] ').strip().upper()[0]
            if continua in 'SN':
                break
        except IndexError:
            pass
        print('Valor inválido. Tente novamente')
    if continua == 'N':
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {homem}')
print(f'Temos {mulher_menor_20} {"mulher" if mulher_menor_20 == 1 else "mulheres"} com menos de 20 anos')

