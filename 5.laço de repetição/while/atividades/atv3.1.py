import os
os.system('c')


#variaveis
login= "admin123"
senha= "123456"
#entrada

#processamento
for i in range(3):
    input_login= input("Digite seu login: ")
    input_senha= input("Digite sua senha: ")
    if input_login == login and input_senha == senha:
        print("BEM-VINDO")
        break
    else:
        print("LOGIN OU SENHA INCORRETOS")
        if i == 2:
            print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS")
            break


#saida
