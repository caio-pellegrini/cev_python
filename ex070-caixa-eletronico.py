print('-=' * 20)
print(f'{"CAIÃO PROMOÇÃO" :^40}')
print('-=' * 20)
total = mais_caro = cont = 0
mais_barato = [0, '']
while True:
    # produto
    produto = input('Nome do produto: ')

    # preço
    preco = float(input('Preço do produto: R$').replace(',', '.'))

    # analise dos dados
    total += preco
    cont += 1

    if preco > 1000:
        mais_caro += 1

    if cont == 1 or preco < mais_barato[0]:
        mais_barato[0] = preco
        mais_barato[1] = produto

    # quer continuar?
    while True:
        try:
            resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
            if resposta in 'SN':
                break
        except IndexError:
            pass
        print('[Valor Inválido] ', end='')
    if resposta == 'N':
        break
    else:
        print('-' * 35)
print(f'\n{"FIM DO PROGRAMA" :+^45}\n')
print(f'Você comprou {cont} produtos e o total da compra foi R${total:.2f}')
print(f'Temos {mais_caro} {"produto" if mais_caro == 1 else "produtos"} custando mais que R$1000.00')
print(f'O produto mais barato foi {mais_barato[1]}, que custou R${mais_barato[0]:.2f}')
