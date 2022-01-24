cont = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? (0 ou n negativo para parar) '))
    print('-' * 50)
    if valor <= 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c:>2} = {valor * c:>2}')
    cont += 1
    print('-' * 50)
print(f'PROGRAMA DA TABUADA encerrado. Você vizualizou a tabuada de {cont} valores')