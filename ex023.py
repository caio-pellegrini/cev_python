num = int(input('Digite um número entre 0 e 9999: '))
print(f'Analisando o número {num}')
# divide e obtem um numero inteiro, que por sua vez exibirá o resto da divisão por 10
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
