import os
os.system('cls')

while True:
    nota1=int(input("Digite a primeira nota: "))
    nota2=int(input("Digite a segunda nota: "))

    if nota1 | nota2 < 0 or nota1 | nota2 > 10:
        print("Repetindo...")
    else:
        break
#saida
print(f"Sua primeira nota é: {nota1}")
print(f"Sua segunda nota é: {nota2}")
    