import os
os.system('clear')

contador= 0
soma= 0
while True:
    valor= int(input("Digite um valor (inteiro): "))
    if valor < 0:
        break
    else:
        contador += 1
        soma+= valor



#evita divisão por zero
if contador == 0:
    soma = valor
    contador = 1

media=  soma / contador

print(f"A média dos valores é: {media}")

