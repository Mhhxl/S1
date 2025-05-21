import os
os.system('cls || clear')




#criando função para calcular a média
def caucular_media(lista_notas):
    soma = sum(lista_notas) 
    media = soma / 4
    return media


#criando lista que vair receber 4 notas
lista_notas = []
for i in range(4):
    nota= float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)

#colocando a variavel media pra jogo
media= caucular_media(lista_notas)
#verificando se a média é maior ou igual a 7
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')


#exibindo resultados
print()
print(f'As notas são: {lista_notas}')
print(f"média: {media:.2f}")