salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    aumento = 10
else:
    aumento = 15

novo_salario = salario + (aumento/100 * salario)
print(f'O funcionário que recebia \033[35mR${salario :.2f}\033[m, passa a receber \033[1;32mR${novo_salario :.2f}\033[m')
print(f'Isso representa um aumento de \033[1;33m{aumento}%')