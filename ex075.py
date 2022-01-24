valores = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))

print(f'Você digitou os valores {valores}')

print(
    f'O valor {valores[0]} apareceu {valores.count(valores[0])} {"vez" if valores.count(valores[0]) == 1 else "vezes"}')

print(f'O valor {min(valores)} apareceu na {valores.index(min(valores)) + 1}º posição')

print(f'Os valores pares digitados foram: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
