import os
os.system('clear')
print("seja bem vindo ao nosso estabelecimento")

#entrada
opcao=int(input("""
Código \t Prato \t\t valor
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\t R$ 20,00
    3 \t Strogonoff \t\t R$ 18,00
    4 \t Bife acebolado \t R$ 15,00
    5 \t Pão com ovo \t\t R$ 5,00
    Digite a opção desejada:
"""))
#esse é o menu que irá aparecer para o usuario

#o comando \t é para dar um espaço entre as palavras

#o comando \n é para pular uma linha

#o comando """ é para que o texto fique entre aspas triplas, e assim, possa ser escrito em mais de uma linha




#processamento
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
#saída
print(f"O valor do prato é R$ {valor:.2f}")
print("Obrigado pela preferência")


#o comando :.2f é para que o valor seja mostrado com 2 casas decimais