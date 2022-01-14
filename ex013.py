salario = float(input('Qual o salário atual do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print(f'Com o ajuste salarial de 15%, o funcionário que ganhava R${salario :.2f} passa a ganhar R${novo :.2f}.')
print(f'Foi um aumento de R${novo - salario :.2f}.')
