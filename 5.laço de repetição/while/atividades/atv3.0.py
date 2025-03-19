import os
os.system('cls')


login= "marta"
senha= "123"

while True:
    login_input= input("Digite seu login: ")
    senha_input= input("Digite sua senha: ")

    if login_input == login and senha_input == senha:
        print("acesso permitido")
        break
    else:
        print("acesso negado")
        #forma que o professor faz