import os
os.system('cls || clear')

#pedindo ao usuario as notas
nota = 0
for i in range(1, 3):
    nota += float(input(f'Digite a {i}ª nota: '))
#função para calcular a média
def calcular_media(i):
    media = i / 2
    return media

#resultado da média (aprovado, reprovado)
if calcular_media(nota) >= 7:
    print(f'A média é: {calcular_media(nota)} - Aprovado')
else:
    print(f'A média é: {calcular_media(nota)} - Reprovado')