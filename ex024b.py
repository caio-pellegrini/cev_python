cidade = input('Em que cidade você nasceu? ').strip().capitalize()

tof = 'Santo' in cidade.replace(' ', '')
# print(tof)

print(f'A cidade que você nasceu {"começa" if tof else "não começa"} a palavra "Santo"')