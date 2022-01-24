from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('Essas são suas opções:')
# sleep(1)
opcoes = """
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior valor
    [ 4 ] Novos números
    [ 5 ] Sair do programa"""
# sleep(2)
print(opcoes)
opcao = int(input('\n>>> Qual é a sua opção? '))
while opcao != 5:
    if 1 <= opcao < 5:
        if opcao == 1:
            sleep(1)
            print(f'\033[31mA soma entre {n1} e {n2} é igual a {n1 + n2}\033[m')
        if opcao == 2:
            sleep(1)
            print(f'\033[32mA multiplicação entre {n1} e {n2} é igual a {n1 * n2}\033[m')
        if opcao == 3:
            sleep(1)
            print(f'\033[33mO maior valor é {max([n1, n2])}\033[m')
        if opcao == 4:
            sleep(1)
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