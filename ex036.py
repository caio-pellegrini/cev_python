from time import sleep
print('----- APROVADOR DE EMPRÉSTIMO -----')
valor = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos de finanaciamento? '))
tempo = anos * 12
prestacao = valor / tempo
sleep(1)
print('Calculando...')
sleep(2)
print(f'O valor da casa é de R${valor :.2f} e a prestação mensal será de R${prestacao :.2f}, durante {int(tempo)} meses')
trinta_salario = salario * 0.3
if prestacao > trinta_salario:
    print(f'\033[31mEmprestimo NEGADO\033[m, pois o valor da prestação é maior do que 30% do salário (R${trinta_salario :.2f})')
else:
    print(f'\033[32mEmpréstimo CONCEDIDO!\033[m Aproveite sua casa nova!')