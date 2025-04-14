import os
os.system('cls || clear')



#variaveis
nota= 0
#recebendo notas
for i in range (1, 3):
    nota+=float(input(f"Digite sua {i}ª nota:"))
    


#cauculando média
def caucular_media(i):
    media = i /2 
    return media

#informando média
def informar_media():
    if media >= 7:
        print("Aprovado")
    else: 
        print("reprovado")


media= caucular_media(nota)
print(f"Média: {media}")
resultado= informar_media()