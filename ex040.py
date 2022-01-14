n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média desse aluno é {media :.1f}')
if media > 7:
    print(f'O aluno está \033[32mAPROVADO')
elif 5 <= media <= 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO')
else:
    print('O aluno está \033[31mREPROVADO')