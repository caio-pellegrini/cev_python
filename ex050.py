soma = 0
cont = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números pares e a soma foi {soma}.')
