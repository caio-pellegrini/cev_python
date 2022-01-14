print('=-' * 20)
print('EX 035 ---- ANALISADOR DE TRIANGULOS 1.0')
print('=-' * 20)

a = float(input('\033[97;43mPrimeiro segmento:\033[m '))
b = float(input('\033[31mSegundo segmento:\033[m '))
c = float(input('\033[36;107mTerceiro segmento:\033[m '))

if a + b > c and b + c > a and a + c > b:
    print('Com esses três segmentos \033[4;30;44mé possível\033[m formar um triângulo!')
else:
    print('Com esses três segmentos \033[1;36;40mé impossível\033[m formar um triângulo!')

