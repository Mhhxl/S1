import os
os.system("Cls || clear")

def logo_senai():
    os.system(' cls || clear')
    print("==SENAI DENDEZEIROS==")
    
    
def multiplicar(n1, n2):
    return n1 * n2

logo_senai()
num1=int(input("Digite o primeiro número: "))

logo_senai()
num2=int(input("Digite o segundo número: "))

multiplicacao= multiplicar(num1, num2)
print(f"A multiplicação é : {multiplicacao}")
