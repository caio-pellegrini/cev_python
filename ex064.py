num = soma = 0
c = -1
while num != 999:
    c += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Ao todo, você digitou {c} {"número" if c == 1 else "números"} e a soma entre eles foi {soma}')