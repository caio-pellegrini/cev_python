n = int(input('Digite um número inteiro para ver sua tabuada: '))

print(f'\nImprimindo a tabuada do número {n}')
print('-'*20)

for tab in range(1, 11):
    print(f'{n} x {tab :2} = {n*tab :2}')

print('-'*20)
