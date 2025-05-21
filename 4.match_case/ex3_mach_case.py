import os 
os.system('clear')

idade=input("DIGITE SUA IDADE: ")

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