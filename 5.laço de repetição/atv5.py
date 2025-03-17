import os
os.system('clear')

print("somando numeros")
soma = 0
for i in range(1, 6): 
    nota= float(input(f"digite a {i}ª nota: "))
    #soma =soma + nota
    soma += nota
print(f"A soma das notas é {soma}")

print()
print("\nFim do programa")
print()