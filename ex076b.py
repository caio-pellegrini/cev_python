print('♦' * 40)
print(f'{"CARDÁPIO VOLTA AS AULAS":^40}')
print('♦' * 40)
produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.90)

for prod in range(0, len(produtos), 2):
    print(f"{produtos[prod]:.<36}R$ {produtos[prod+1]:>6.2f}")