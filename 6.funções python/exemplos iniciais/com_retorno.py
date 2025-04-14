import os
os.system("Cls || clear")


#função com retorno
def caucular_media(primeira_nota,  segunda_nota):
    soma= primeira_nota + segunda_nota
    media= soma /2
    return media
    

def logo_senai():
    os.system("Cls || clear")
    print("=SENAI==")


logo_senai()
primeiro_numero= int(input("Digite o primeiro numero: "))

logo_senai()
segundo_numero= int(input("Digite o segundo numero: "))

media= caucular_media(primeiro_numero, segundo_numero)

print(f"Média: {media}")