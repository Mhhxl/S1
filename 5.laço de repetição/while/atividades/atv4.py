import os
os.system('cls || clear')

#variaveis \ constantes
notas = 3
soma= 0

for i in range(notas): 
    nota = float(input("Digite a nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida")
    else: 
        soma += nota
        break


media= soma / notas
if media >= 7:
    resultado="Aprovado"
elif media >= 5:
    resultado="Recuperação"
else:
    resultado="Reprovado"
print(f"a média é {media}")
print(f"o resultado é {resultado}")
