import os

os.system ("cls")


print("==BEM-VINDO==")

idade=(input("DIGITE SUA IDADE:  "))
#o comando não estava funcionando pois eu armazenava um valor numerico, e tudo oq esta entre "" recebe um valor string

#possiveis soluções: retirar o valor numerico, ou retirar as "" de cada numero usado no match case, pois elas armazenam um valor string
match idade:
    case "13":
        print("acesso negado, menor de idade")
    
    case "14":
        print("acesso negado, menor de idade")
    
    case "15":
        print("acesso negado, menor de idade")

    case "16":
        print("somente com a permissão dos pais")
        
    case "17":
        print("somente com a permissão dos pais")
        
    case "18":
        print("acesso permitido")
        
    case "19":
        print("acesso permitido")
        
    case _:
        print("invalido, por favor tente novamente")
        
print(f"sua idade é: {idade}")
        

print("==FIM==")
