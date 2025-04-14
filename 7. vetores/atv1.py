import os
os.system('cls || clear')
    
    
    
    
#criando função para calcular a média
def caucular_media(lista_notas):

    soma = sum(lista_notas) 
    media = soma / 3
    return media
#criando função para verificar se a média é maior ou igual a 7



#criando lista de notas
lista_notas = []

#adicionando 3 notas dentro da lista
for i in range(3):
    nota= float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)


#exibindo resultados
media= caucular_media(lista_notas)
print(f'As notas são: {lista_notas}')
print(f"média: {media:.2f}")