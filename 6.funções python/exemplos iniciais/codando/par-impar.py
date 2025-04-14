import os
os.system('cls || clear')

#entrada
def numero():
    num=int(input("Digite um número: "))
    if num % 2  == 0:
        print("é par")
    else: 
        print("é impar")
        
numero()
