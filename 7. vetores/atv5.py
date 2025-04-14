import os
os.system('cls || clear')

def par_ou_impar(num):
   
    par = 0
    impar = 0
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
        return par, impar
#criando lista de numeros
lista_num= []
quantidade_numeros = 6
par_ou_impar = (lista_num)
print("== SOLICITANDO NUMEROS==")
for i in range(quantidade_numeros):
    num = int(input(f"Digite o {i+1}º número: "))
    lista_num.append(num)

print(f"pares :{par_ou_impar(lista_num)}")
print(f"impares :{par_ou_impar(lista_num)}")