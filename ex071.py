print('+-' * 22)
print(f'{"BANCO PELLEGRINI":^44}')
print('+-' * 22)
print('Boa tarde, hoje temos notas de R$50, de R$20, de R$10 e de R$1')
sacar = int(input('Quanto você deseja sacar? '))
cedulas50 = sacar // 50
if cedulas50 != 0:
    sacar -= 50 * cedulas50
    print(f'Você retirou {cedulas50} cédulas de R$50.00')
cedulas20 = sacar // 20
if cedulas20 != 0:
    sacar -= 20 * cedulas20
    print(f'Você retirou {cedulas20} cédulas de R$20.00')
cedulas10 = sacar // 10
if cedulas10 != 0:
    sacar -= 10 * cedulas10
    print(f'Você retirou {cedulas10} cédulas de R$10.00')
cedulas1 = sacar // 1
if cedulas1 != 0:
    sacar -= cedulas1
    print(f'Você retirou {cedulas1} cédulas de R$1.00')
print('=' * 40)
print('Volte sempre!')
