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

for index, prod in enumerate(produtos):
    if index % 2 == 0:
        print(f"{prod:.<36}R$ ", end='')
    else:
        print(f"{prod:>6.2f}")