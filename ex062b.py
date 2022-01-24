print(f'Gerador de PA \n{"=+" * 10}')
num = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
resultado = num
print('MOSTRANDO OS 10 PRIMEIROS TERMOS')
contador = 0
vezes = 10
while vezes > 0:
    for c in range(vezes):
        print(resultado, end=' -> ')
        resultado += razao
        contador += 1
    print('PAUSA')
    vezes = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {contador} termos mostrados')
