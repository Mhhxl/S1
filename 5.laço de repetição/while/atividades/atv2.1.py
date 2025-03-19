import os
os.system('clear')

notas= 2
soma = 0
for i in range (notas):
    while True:
        nota= int(input(f"Digite uma nota: "))
        if nota < 0 or nota > 10:
            print("A nota deve ser entre 0 e 10")
        else:
            soma += nota
            break
media = soma / notas
print(f"A média das notas é: {media:.2f}")
#forma que o professor faz