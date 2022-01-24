continua = ''
soma = cont = maior = menor = 0
while continua != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    continua = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continua not in 'SN':
        print('Valor inávalido. A resposta foi automaticamente escolhida como S')

print(f'Você digitou {cont} números e a média entre eles foi {soma / cont :.1f}')
print(f'Maior número: {maior}. Menor número: {menor}')
