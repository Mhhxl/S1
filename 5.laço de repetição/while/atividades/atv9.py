import os
os.system('clear')



idade = int
sexo = str
salario = float
#entrada 
escolha=(input("""Código \t|  Descrição\n
    1 \t|  Adicionar Pessoa
    2 \t|  Exibir Resultados
    3 \t|  Sair
                """))

match escolha:
    case "1":
        idade=int(input("informe sua idade: "))
        sexo=(input("informe seu sexo: "))
        salario=float(input("informe seu salário: "))
    case "2":
        print(f"Sua idade é: {idade}")
        print(f"Seu Sexo é: {sexo} ")
        print(f"Seu Salário é: {salario}")
    case "3":
        SystemExit
    case _:
        print("Opção inválida")
