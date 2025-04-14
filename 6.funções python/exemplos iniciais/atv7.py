import os
os.system('cls || clear')
nota=0
for i in range(1,3):
    nota+= float(input(f'Digite a {i}ª nota: '))


def caucular_media(i):
    media= i / 2
    return media

print(f'A média é: {caucular_media(nota)}')