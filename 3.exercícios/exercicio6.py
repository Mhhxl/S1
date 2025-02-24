import os
os.system ("clear")

#variavel
senha = "1234"
login = "admin"

input_login = input("Digite seu login: ")
input_senha = input("Digite sua senha: ")
print("SEU LOGIN É: ", input_login)
print("SUA SENHA É: ", input_senha)
if input_login == login and input_senha == senha:
    print("BEM-VINDO")
else:
    print("LOGIN OU SENHA INCORRETOS")


print("==FIM==")