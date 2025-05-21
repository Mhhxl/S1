import os
os.system('cls || clear')

def positivo_negativo(valor):
    if valor < 0:
        print("é negativo")
    elif valor == 0: 
        print("é neutro")
    else: 
        print("é positivo")

num=int(input("Digite um número: "))
positivo_negativo(num)