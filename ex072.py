numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezessesis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número \033[31;40m{numeros[numero]}\033[m')
        print('---------------')
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resposta == 'N':
            break
        elif resposta not in 'SN':
            print('Resposta inválida. ', end='')
    else:
        print('Valor inválido. Tente novamente')
print('OK. Fechando programa')
