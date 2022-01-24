print(f'Gerador de PA \n{"=+" * 10}')
num = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
resultado = num
print('MOSTRANDO OS 10 PRIMEIROS TERMOS')
for c in range(10):
    print(resultado, end=' -> ')
    resultado += razao
print('PAUSA')
contador = 10
vezes = 1
while vezes > 0:
    vezes = int(input('Quantos termos você quer mostrar a mais? '))
    if vezes != 0:
        for c in range(vezes):
            print(resultado, end=' -> ')
            resultado += razao
            contador += 1
        print('PAUSA')
    else:
        print(f'Progressão finalizada com {contador} termos mostrados')
