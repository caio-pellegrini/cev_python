soma = cont = 0
produto = 1
while True:
    n = int(input('Digite um número: (999 para parar) '))
    if n == 999:
        break
    soma += n
    cont += 1
    produto *= n
print(f'Você digitou \033[31m{cont} valores\033[m')
print(f'A \033[32msoma\033[m entre eles foi \033[32m{soma}\033[m')
print(f'O \033[33mproduto\033[m entre eles foi \033[33m{produto}\033[m')
