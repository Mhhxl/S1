import os
os.system('cls || clear')




#criando função para calcular a média
def caucular_media(lista_notas):
    soma = sum(lista_notas) 
    media = soma / 4
    return media

#adicionando função para verificar se a média é maior ou igual a 7
def verificar_aprovacao(media):
    if media >= 7:
        resultado= 'Aprovado'
    elif media >= 5:
        resultado= 'Recuperação'
    else:
        resultado= 'Reprovado'
    return resultado

#criando lista que vair receber 4 notas
lista_notas = []
for i in range(4):
    nota= float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)

#colocando a variavel media pra jogo
media= caucular_media(lista_notas)


#exibindo resultados
print()
print(f'As notas são: {lista_notas}')
print(f"média: {media:.2f}")
print(f"Situação: {verificar_aprovacao(media)}")