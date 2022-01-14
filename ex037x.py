print('\033[107;30m=-==-= CONVERSOR DE NÚMEROS =-= EX 037 =-==-=\033[m')

n = int(input('Digite um número inteiro: '))
bi = '\033[1;31mBINÁRIO\033[m'
oc = '\033[1;36mOCTAL\033[m'
hx = '\033[1;34mHEXADECIMAL\033[m'
print(f'''Escolha uma das bases para conversão:
[ 1 ] Converter para {bi}
[ 2 ] Converter para {oc}
[ 3 ] Converter para {hx}
[ 0 ] Converter para todos os acima''')
opcao = input('Sua opção: ').strip()
op1 = f'O número \033[97m{n}\033[m em {bi} é \033[97m{n:b}\033[m'
# outra forma, mostrada no video: .format(n, bin(n)[2:]
op2 = f'O número \033[97m{n}\033[m em {oc} é \033[97m{n:o}\033[m'
op3 = f'O número \033[97m{n}\033[m em {hx} é \033[97m{n:x}\033[m'
if opcao == '1':
    print(op1)
elif opcao == '2':
    print(op2)
elif opcao == '3':
    print(op3)
elif opcao == '0':
    print(f'{op1}\n{op2}\n{op3}')
else:
    print('Foi mal, não consegui entender o que você digitou')
