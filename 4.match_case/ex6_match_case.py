import os 
os.system ("clear")


#variáveis/ constantes



#entrada de dados
valor_do_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int (input("""Digite a forma de pagamento: 
1- A vista: 
2- A prazo: """))

#processamento de dados
match forma_de_pagamento:
    case 1:
        #aplicando 10% de desconto
        desconto = valor_do_produto * 0.10
        print(f"O valor do produto com desconto é de R${valor_do_produto - desconto}")
    case 2: 
        valor_do_produto = valor_do_produto / 6
        input("Digite a quantidade de parcelas: ")

    