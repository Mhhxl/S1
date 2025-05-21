import os
os.system('cls || clear')

#entrada
soma = 0
opcao=int(input("""
Código \t Prato \t\t valor
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\t R$ 20,00
    3 \t Strogonoff \t\t R$ 18,00
    4 \t Bife acebolado \t R$ 15,00
    5 \t Pão com ovo \t\t R$ 5,00
    Digite a opção desejada:
"""))

#processamento
while True:
    match opcao:
        case 1:
            print("Você escolheu Picanha")
            valor=25.00
        case 2:
            print("Você escolheu Lasanha")
            valor=20.00
        case 3:
            print("Você escolheu Strogonoff")
            valor=18.00
        case 4:
            print("Você escolheu Bife acebolado")
            valor=15.00
        case 5:
            print("Você escolheu Pão com ovo")
            valor=5.00
        case _:
            print("Opção inválida")
            valor=0

    soma += valor
    continuar= input("Deseja continuar? [s/n] ")
    if continuar == "n":
        break
#saída
