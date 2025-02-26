import os
os.system ("clear")

dia=int(input("DIGITE UM DIA: ") )
#retirei o comando int (no vs code, enquanto testava com idades) pois ele estava armazenando um valor numerico, e tudo oq esta entre "" recebe um valor string
match dia:
    case 2:
        print("Hoje é segunda-feira")
    case 3:
        print("Hoje é terça-feira")
    case 4:
        print("Hoje é quarta-feira")
    case 5:
        print("Hoje é quinta-feira")
    case 6:
        print("Hoje é sexta-feira")
    case 7 :
        print("Hoje é sábado")
    case 1 :
        print("Hoje é domingo")
    case _:
        print("Dia inválido")
# o comando _ é o "default", caso não seja nenhum dos casos acima
print (f"HOJE É DIA: {dia}")


