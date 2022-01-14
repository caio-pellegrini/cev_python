print('CONTAGEM DE NÚMEROS PARES')
nmin = int(input('Em que número eu devo começar? '))
nmax = int(input('Até que número eu devo contar? '))
if nmin > nmax or nmin < 0 or nmax < 0:
    print('Os números devem ser maiores que 0 e o segundo número deve ser maior que o primeiro!')
else:
    contador = 0
    nmpar = False if nmin == 1 else nmin // 2 == 0
    print(nmpar)
    for c in range(nmin if nmpar else nmin+1, nmax+1, 2):
        print(c)
        contador += 1
    print(f'De {nmin} até {nmax} existem {contador} números pares')
