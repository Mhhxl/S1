import os
os.system('cls || clear')

#criando lista de numeros
lista_num= []
#programa pra ler 5 numeros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    lista_num.append(num)

#separando o maior do menor
maior = max(lista_num)
menor = min(lista_num)

print(f"{lista_num} \nO maior número é {maior} e o menor número é {menor}")
print(f"os numeros são: {lista_num}")