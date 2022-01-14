# NO USE THISSS, GO TO ex033a or ex033c
# JUST TESTING
print('Digite três valores diferentes')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 < n2 and n1 < n3:
    menor = n1
    if n2 > n3:
        maior = n2
    else:
        maior = n3
    print(f'O menor valor digitado foi {menor}')
    print(f'O maior valor digitado foi {maior}')
elif n2 < n1 and n2 < n3:
    menor = n2
    if n1 > n3:
        maior = n1
    else:
        maior = n3
    print(f'O menor valor digitado foi {menor}')
    print(f'O maior valor digitado foi {maior}')
elif n3 < n1 and n3 < n2:
    menor = n3
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print(f'O menor valor digitado foi {menor}')
    print(f'O maior valor digitado foi {maior}')
else:
    print('Você não digitou valores diferentes!')