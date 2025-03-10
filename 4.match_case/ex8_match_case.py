import os
os.system("clear")

#cauculo de peso ideal

print("BEM-VINDO") 
print("Vamos calcular seu peso ideal" )
print("Qual e o seu gênero?")
Genero = input("Digite M para masculino e F para feminino: ")
Altura: float
PesoIdeal: float
match Genero:
    case "M" | "m":
        Altura = float(input("Digite sua altura: "))
        PesoIdeal = (72.7 * Altura) - 58
        print(f"Seu peso ideal é: {PesoIdeal:.2f}:")

    case "F" | "f":
        Altura = float(input("Digite sua altura: "))
        PesoIdeal = (62.1 * Altura) - 44.7
        print(f"Seu peso ideal é: {PesoIdeal:.2f}: ")
    case _:
        print("Gênero inválido")
print("Obrigado por usar nosso programa")
# = serve para atribuir um valor a uma variavel
# : serve pra definir o tipo de variavel
# .2f serve para limitar a quantidade de casas decimais