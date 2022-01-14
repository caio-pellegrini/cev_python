from time import sleep

print(f'{" EX 033 C " :=^25}')
print('Você está prester a usar uma calculadora \033[97;40msuper-hiper-mega inteligente\033[m')
sleep(2)
print('\033[36mSiga as instruções e seja cauteloso... \033[m', end="")
sleep(1.5)
print('Depois de um passo em falso, \033[31mtalvez não dê \npara voltar atrás...\033[m')

print('')
sleep(1)
n1 = float(input('\033[1mDigite um número.\033[m Pode ser inteiro ou real: '))
sleep(0.5)
n2 = float(input('Certo! Número salvo. Agora \033[1;33;107mdigite um segundo número:\033[m '))
sleep(0.8)
n3 = float(input('OK. \033[34mÚltimo número agora:\033[m '))

lista = [n1, n2, n3]

resp = input('Você deseja saber o menor número ou o maior? Digite + para maior e - para menor.\nSe quiser saber dos dois digite outra coisa. ')
lista = sorted(lista)
menor = lista[0]
maior = lista[2]

if resp == '-':
    print(f'O \033[31mmenor\033[m número é \033[31m{menor}\033[m')
elif resp == '+':
    print(f'O \033[32mmaior\033[m número é \033[32m{maior}\033[m')
else:
    print(f'O \033[31mmenor\033[m número é \033[31m{menor}\033[m')
    print(f'O \033[32mmaior\033[m número é \033[32m{maior}\033[m')
