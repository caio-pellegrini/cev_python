print('+-' * 22)
print(f'{"BANCO PELLEGRINI":^44}')
print('+-' * 22)
print('Boa tarde, hoje temos notas de R$50, de R$20, de R$10 e de R$1')
valor = int(input('Quanto você deseja sacar? '))
total = valor
cedula = 50
total_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Você retirou {total_ced} cédulas de R${cedula},00')
            total_ced = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        if total == 0:
            break
print('=' * 40)
print('Volte sempre!')