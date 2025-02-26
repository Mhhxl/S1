import os
os.system('clear')

#entrada
primeiro_numero = int(input("Digite o primeiro número: "))
operador = input("Digite a operação que deseja (+ - * /):")
segundo_numero = int(input("Digite o segundo número: "))

#processamento
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Operador inválido")
        resultado = 0
#saída

print(f"O resultado da operação é:  {resultado}") 
print(f"operação {operador}")
print(f"primeiro número {primeiro_numero}")
print(f"segundo número {segundo_numero}")