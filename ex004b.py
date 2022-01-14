valor = input('Digite algo: ')
print(f'Você digitou {valor}')
print(f'O tipo primitivo desse valor é {type(valor)}')

caio
def son(arg):
    if arg == 'False':
        return 'Não'
    elif arg == 'True':
        return 'Sim'


print(f'Só tem espaços? {son(valor.isspace())}')
print(f'É um número? {son(valor.isnumeric())}')
print(f'É alfabético? {son(valor.isalpha())}')
print(f'É alfanúmerico? {son(valor.isalnum())}')
print(f'Está em maiúsculas? {son(valor.isupper())}')
print(f'Está em minúsculas? {son(valor.islower())}')
print(f'Está capitalizada? {son(valor.istitle())}')
