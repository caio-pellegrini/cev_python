a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        trian = '\033[1;35mEQUILÁTERO\033[m'
    elif a == b or b == c or a == c:
        trian = '\033[1;34mISÓCELES\033[m'
    else:
        trian = '\033[1;36mESCALENO\033[m'
    print(f'Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo {trian}.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo.')