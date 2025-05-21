import os
os.system ("clear")

print ("SEJA BEM VINDO")
#variaveis  

#pedindo informações ao usuário
    
maçãs = int(input("Quantas maçãs você deseja comprar? "))
if maçãs < 12:
    preço= 1.30
else:
    preço= 1.00

total= maçãs * preço

print(f"O preço total é: {total}")
