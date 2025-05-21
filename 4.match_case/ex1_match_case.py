import os
os.system ("clear")

dia=input("DIGITE UM DIA: ") 
#retirei o comando int (no vs code, enquanto testava com idades) pois ele estava armazenando um valor numerico, e tudo oq esta entre "" recebe um valor string

# o comando match case é uma forma mais simples de fazer um if else

# ele compara o valor da variável com os valores dos casos

# e executa o comando do caso que for igual ao valor da variável

# caso não seja igual a nenhum caso, ele executa o comando do default

# o comando match case é mais simples e mais rápido que o if else


match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terça":
        print("Hoje é terça-feira")
    case "quarta":
        print("Hoje é quarta-feira")
    case "quinta":
        print("Hoje é quinta-feira")
    case "sexta":
        print("Hoje é sexta-feira")
    case "sábado":
        print("Hoje é sábado")
    case "domingo":
        print("Hoje é domingo")
    case _:
        print("Dia inválido")
# o comando _ é o "default", caso não seja nenhum dos casos acima





