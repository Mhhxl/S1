import os
os.system("Cls || clear")

def logo_senai():
    os.system(' cls || clear')
    print("==SENAI DENDEZEIROS==")
    
def somando(n1, n2):
    return n1 + n2     

logo_senai()
num1=int(input("Digite o primeiro número: "))


logo_senai()
num2=int(input("Digite o segundo número: "))

logo_senai()
soma = somando(num1, num2)
print(f"a soma é: {soma}")


#primeiro criei uma função para limpar o terminal e em seguida exibir a mensagem do senai dendezeiros

#depois criei uma segunda função (com retorno) para realizar a soma de duas variaveis

#depois eu usei a primeira função nas duas variaveis q criei pra limpar o terminal e exibir a msg do senai

#e por ultimo criei uma terceira variavel que recebe a função, e a função recebe o cauculo matématico da soma


