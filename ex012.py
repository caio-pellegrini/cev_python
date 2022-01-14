preco = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${preco :0.2f} na promoção com um desconto de 5% agora está custando R${preco - (preco * 5 / 100) :0.2f}.')