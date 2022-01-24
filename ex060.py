# da maneira que eu resolvi inicialmente

"""
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
calculo = num
chegou_no_1 = False
print(f'{num}! = {num}', end='')
while not chegou_no_1:
    c -= 1
    calculo = calculo * c
    print(f' x {c}', end='')
    if c == 1:
        chegou_no_1 = True
print(f' = {calculo}')"""

# da maneira feita na aula

num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'{num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(" x " if c > 1 else " = ", end='')
    f *= c
    c -= 1
print(f)
