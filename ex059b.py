from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('Essas são suas opções:')
# sleep(1)
opcoes = """
    [ 1 ] Somar
    [ 2 ] Concatenar
    [ 3 ] Multiplicar
    [ 4 ] Maior valor
    [ 5 ] Comparar com salário de Elon Musk
    [ 6 ] Novos números
    [ 0 ] Sair do programa"""
# sleep(2)
print(opcoes)
opcao = int(input('\n>>> Qual é a sua opção? '))
while opcao != 0:
    if 0 <= opcao <= 6:
        # sleep(0.8)
        if opcao == 1:
            print(f'\033[31mA soma entre {n1} e {n2} é igual a {n1 + n2}\033[m')
        elif opcao == 2:
            print(f'\033[32mAo concatenarmos esses valores, obtemos {str(n1) + str(n2)}.\033[m')
        elif opcao == 3:
            print(f'\033[33mA multiplicação entre {n1} e {n2} é igual a {n1 * n2}\033[m')
        elif opcao == 4:
            if n1 == n2:
                print('\033[34mOs dois valores são iguais!\033[m')
            else:
                print(f'\033[34mO maior valor é {max([n1, n2])}\033[m')
        elif opcao == 5:
            porcentagem = 100 * (n1 + n2) / 1350000
            print(f'\033[35mA soma dos valores digitados equivalem a {porcentagem :.6f}% do que Elon Musk ganha por hora!\033[m')
        elif opcao == 6:
            print('OK, vou te solicitar dois novos números...\n')
            sleep(1)
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        sleep(0.75)
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        sleep(0.5)
        print('O que deseja fazer agora?')
    else:
        print('Opção inválida. Tente novamente')
        sleep(0.5)
    print(opcoes)
    opcao = int(input('\n>>> Qual é a sua opção? '))
print('Obrigado por usar nosso programa!')