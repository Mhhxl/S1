import os
os.system('clear')
pares=0
impares=0
print("numeros pares e impares: ")
for i in range (5):
    numero=int(input("digite um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"numeros pares: {pares}")
print(f"numeros impares: {impares}")


print("fim do programa")
