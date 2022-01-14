n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O \033[42;97mprimeiro valor\033[m é \033[1;32;107mMAIOR\033[m')
elif n2 > n1:
    print('O \033[41;97msegundo valor\033[m é \033[1;31;107mMAIOR\033[m')
elif n1 == n2:
    print('\033[43;30mOs dois valores\033[m são \033[1;33;40mIGUAIS\033[m')
else:
    print('\033[31mERRO!')
