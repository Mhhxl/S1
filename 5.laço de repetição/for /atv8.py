import os
os.system('clear')


#entrada
soma= 0

print("notas:")

#processamento
for i in range(4):
    nota = float(input("digite a nota: "))
    soma += nota
media = soma / 4

print("\nResultado:")
if media >= 7:
    print(f"media: {media}")
    print("aprovado")
elif media >= 4 and media < 7:
    print(f"media: {media}")
    print("recuperação")
else:
    print(f"media: {media}")
    print("reprovado")

#saida
print("FIM DO PROGRAMA")
