import os
os.system('clear')

while True:
    nota1=int(input("Digite a primeira nota: "))
    nota2=int(input("Digite a segunda nota: "))

    if nota1 | nota2 < 0 or nota1 | nota2 > 10:
        print("Repetindo...")
    else:
        break
média= (nota1+nota2)/2

#saida
print(f"Sua primeira nota é: {nota1}")
print(f"Sua segunda nota é: {nota2}")
print(f"Sua média é: {média}")