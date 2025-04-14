import os
os.system('cls || clear')

#criando lista de numeros
lista_num= []
quantidade_numeros = 5

print("== SOLICITANDO NUMEROS==")
for i in range(quantidade_numeros):
    num = int(input(f"Digite o {i+1}º número: "))
    lista_num.append(num)

maior = max(lista_num)
menor = min(lista_num)

print(" \n exibindo numeros")
for i, num in enumerate(lista_num, start=0):
    print(f"{i+1}º número: {num}")

print(f"\nO maior número é {maior} e o menor número é {menor}")
print(f"os numeros são: {lista_num}")