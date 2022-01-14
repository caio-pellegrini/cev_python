idade_grupo = 0
idade_homem_velho = 0
mulheres_ate_20 = 0
homem_velho = ''
mais_pesada = 0
nome_mais_curto = ''
for i in range(1, 5):
    print(f'\033[1;3{i}m------ {i}° PESSOA ------\033[m')
    nome = input(f'Nome: ').strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo: (h/m) ').strip().lower()
    peso = float(input(f'Peso: '))
    idade_grupo += idade
    if sexo == 'h' and idade > idade_homem_velho:
        idade_homem_velho = idade
        homem_velho = nome
    if sexo == 'm' and idade < 20:
        mulheres_ate_20 += 1
    if peso > mais_pesada:
        mais_pesada = peso
        sexo_mais_pesada = sexo
    if len(nome) > len(nome_mais_curto):
        nome_mais_curto = nome
print(f'\nA média de idade do grupo é {idade_grupo / 4} anos')
if homem_velho != '':
    print(f'O homem mais velho é {homem_velho}, com {idade_homem_velho} anos')
if mulheres_ate_20 != 0:
    print(f'Existem {mulheres_ate_20} {"mulher" if mulheres_ate_20 == 1 else "mulheres"} com menos de 20 anos')
print(f'A pessoa mais pesada tem {mais_pesada}kg, e ela não é ', end='')
if sexo_mais_pesada != 'h':
    print('um homem!')
elif sexo_mais_pesada != 'm':
    print('uma mulher!')
print(f'A pessoa (ou uma das pessoas) com o nome mais curto é {nome_mais_curto}, com {len(nome_mais_curto)} caracteres')
