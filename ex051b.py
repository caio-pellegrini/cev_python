print('+' * 40)
print('10 TERMOS DE UMA PA')
print('+' * 40)
n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(0, 10):
    print(n + c * razao, end=' => ')
print('Fim da PA')
