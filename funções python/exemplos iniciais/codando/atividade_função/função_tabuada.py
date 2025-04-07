import os
os.system("cls || clear")

numero=int(input("Digite um número para a tabuada: "))


def tabuada():
    for i in range (1, 11):
        print(f"{numero} X {i}: {numero * i}")
        
tabuada()