from time import sleep
print(f'{" PELLEGRINI MODAS ":=^40}')
sleep(1)
print('Bem vindo a melhor loja de moda masculina da região!\n'
      'Calçados, camisas e camisetas, calças e bermudas, e acessórios.\n'
      'De tudo você encontra aqui!')
sleep(4)
input('Quando estiver terminado suas compras, pressione enter ')
sleep(1)
print('OK, vamos então para o pagamento')
sleep(0.8)
valor = float(input('Quanto você gastou? R$').replace(',', '.'))
sleep(0.7)
print('Certo. Como você deseja pagar?')
sleep(0.5)
print('''[ 1 ] à vista no dinheiro
[ 2 ] à vista no cartão
[ 3 ] em 2x no cartão
[ 4 ] 3x ou mais no cartão''')
sleep(1)
opcao = input('Sua opção: ').strip()
if opcao == '1':
    vfinal = valor - (10 / 100 * valor)
    print(f'O valor final da sua compra será de R${vfinal :.2f} (Você recebeu 10% de desconto!).')
elif opcao == '2':
    vfinal = valor - (5 /100 * valor)
    print(f'O valor final de sua compra será de R${vfinal :.2f} (Você recebeu 5% de desconto!).')
elif opcao == '3':
    print(f'Sua compra será parcelada em 2x de R${valor / 2 :.2f} sem juros')
    print(f'O valor final de sua compra será de R${valor :.2f}')
elif opcao == '4':
    parcelas = int(input('Quantas parcelas? (min 3 e max 10): '))
    if 3 <= parcelas <= 10:
        vfinal = valor + (20 / 100 * valor)
        vparcelas = vfinal / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${vparcelas :.2f} com juros')
        print(f'Total = R${vfinal :.2f} (20% de juros)')
    else:
        print('Número de parcelas inválido')
else:
    print('Essa opção não existe.')
sleep(1)
print('A PELLEGRINI MODAS agradece sua visita! Caso tenha enfrentado algum erro \nna hora do pagamento, favor tente novamente')