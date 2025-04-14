import os
os.system("Cls || clear")


#essa é a função sem retorno
def logo_senai ():
    os.system  ("cls || clear")
    print("==SENAI==")
    
    
    
logo_senai() # = chamando a função
nome = (input("Digite seu nome: "))

logo_senai() # = chamando a função
idade = int(input("Digite sua idade: "))


logo_senai() # = chamando a função 
print(f"nome {nome}")
print(f"idade {idade}")
