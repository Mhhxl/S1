import os
os.system('cls || clear')


def somar (n1,n2):
    soma= n1 + n2
    return soma

def multiplicar(n1,n2):
    multipicacao = n1 * n2
    return multipicacao

def subtrair(n1, n2):
    subtracao = n1 - n2
    return subtracao

def dividir (n1, n2):
    divisao= n1 / n2
    return divisao


num1=float(input("Digite o primeiro numero: "))
num2=float(input("Digite o segundo numero: "))


soma = somar(num1, num2)
multiplicacao= multiplicar(num1, num2)
subtracao= subtrair(num1, num2)
divisao= dividir(num1, num2)
print(f"Soma: {somar}")
print(f"Multipicação: {multiplicar}")
print(f"Subtração: {subtrair}")
print(f"Divisão: {dividir}")

#ta errado