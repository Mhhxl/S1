import os
import time

os.system("cls || clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k= 0

while True:
    print("""
    CÓDIGO  |  DESCRIÇÃO
        1   |  Adicionar Pessoa
        2   |  Exibir Resultados
        3   |  Sair
""")
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            sexo = input("Informe seu Sexo use M ou F:").upper()
            salario= float(input("Digite seu salário: "))
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == "F" and salario >= 5000:
                    mulheres5k += 1
                    os.system("cls || clear")
        case 2:
                if contador > 0:
                   media_salarial = soma_salario / contador
                   print("\n Exibindo Resultados: ")
                   print(f"media salarial do grupo: {media_salarial}")
                   print(f"Maior idade do grupo: {maior_idade}")
                   print(f"Menor idade do grupo: {menor_idade}")
                   print(f"Quantidade de muheres com salário acima de 5k: {mulheres5k}")
                else:   
                   print("\n Não foram informados os dados necessários. ")
                   time.sleep(3)
                   os.system("cls || clear")
        case 3:
              print("\n FIM")
              break
        case _:
              print("Opção inválida")
    time.sleep(3)
    os.system("cls || clear")

