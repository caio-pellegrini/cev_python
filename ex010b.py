import time

print('Bem vindo a PyWallet! Trasnfira seus R$ em US$ para gastar como quiser.')
time.sleep(1)

print(f'Carregando...\n')
time.sleep(2)

din = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Calculando conversão...')
time.sleep(2)

print(f'Com R${din :0.2f} você compra US${din / 5.75 :0.2f}\n')
time.sleep(1)

rsp = input('Deseja transferir? Digite "s" para sim e "n" para não: ')
print('')

if rsp == 's':
    print('OK! Transferindo...')
    time.sleep(2)
    print('Dinheiro transferido com sucesso!')
elif rsp == 'n':
    print('Tudo bem! Processo cancelado.')
else:
    print('Resposta não identificada! O processo foi cancelado.')