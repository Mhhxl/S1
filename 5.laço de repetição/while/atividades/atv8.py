import os
os.system("clear")

pares = 0
impares = 0
contador = 0
soma = 0
while True:
    numeros=int(input(f"Digite o {contador + 1}º numero: "))
    if numeros < 0:
        break
    else:
        contador += 1
        soma += 1
    if numeros %2 == 0:
        pares += 1
    else:
        impares += 1






print(f"Numeros impares: {impares} ")
print(f"Numero pares: {pares}")
print(f"Média de numeros pares : {soma / pares}")
