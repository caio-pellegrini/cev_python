from random import randint as rd

valores = (rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10))
# valores = tuple(rd(1, 10) for t in range(5))

print(f'Os valores sorteados foram: ', end='')
for v in valores:
    print(v, end=' ')

print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')

"""print(f'\nO maior valor sorteado foi {sorted(valores)[4]}')
print(f'O menor valor sorteado foi {sorted(valores)[0]}')"""