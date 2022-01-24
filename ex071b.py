print('+-' * 22)
print(f'{"BANCO PELLEGRINI":^44}')
print('+-' * 22)
print('Boa tarde, hoje temos notas de R$50, de R$20, de R$10 e de R$1')
valor = int(input('Quanto você deseja sacar? '))
cedulas = [50, 20, 10, 1]
for cedula in cedulas:
    if valor // cedula != 0:
        print(f'Você retirou {valor // cedula} cédulas de R${cedula}')
        valor = valor - (cedula * (valor // cedula))
print('=' * 40)
print('Volte sempre!')
