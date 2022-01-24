print(f'Gerador de PA \n{"=+" * 10}')
num = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
resultado = num
c = 0
while c < 10:
    print(resultado, end=' -> ')
    resultado += razao
    c += 1
print('FIM DA PA')
