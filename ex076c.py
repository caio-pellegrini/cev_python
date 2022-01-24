print('♦' * 40)
print(f'{"CARDÁPIO VOLTA AS AULAS":^40}')
print('♦' * 40)
produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor',
            'Compasso', 'Mochila', 'Canetas', 'Livro')

precos = (1.75, 2, 15.9, 25, 4.2, 9.99, 120.32, 22.3, 34.9)

for i in range(len(produtos)):
    print(f'{produtos[i]:.<36}R$ {precos[i]:>6.2f}')
