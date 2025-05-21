import os
os.system ("clear")

print("SEJA BEM VINDO")

numero_um=int(input("DIGITE O PRIMEIRO NUMERO: "))
numero_dois=int(input("DIGITE O SEGUNDO NUMERO: "))


menor= min({numero_um, numero_dois})
maior= max({numero_um, numero_dois})

print(f"primeiro numero : {numero_um}")
print(f"segundo numero : {numero_dois}")

print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")
#O comando (min) e (max) serve para comparar valores e retornar o menor e o maior valor
