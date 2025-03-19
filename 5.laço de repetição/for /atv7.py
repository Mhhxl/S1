import os
os.system('clear')

soma= 0
media = 0

print("notas:")
for i in range(4):
    nota = float(input("digite a nota: "))
    soma += nota
media = soma / 4

print()
print(f"media: {media}")
print("FIM DO PROGRAMA")
