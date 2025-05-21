import os 
os.system('clear')

#entrada de dados

print("BEM-VINDO")
empregado = input("Digite o nome do empregado: ")
idade = int(input("Digite a idade do empregado: "))
matricula = int(input("Digite o número da matrícula do empregado: "))
data = input("Digite a data de nascimento do empregado: ")
tempo= int(input("Digite o tempo de serviço do empregado em anos: "))

#processamento de dados

if idade >= 65 or tempo >=30:
    aposentadoria = "Sim"
else: 
    aposentadoria = "Não"

#saida de dados
print(f"Nome: {empregado}")
print(f"Idade: {idade}")
print(f"Número da matrícula: {matricula}")
print(f"Data de nascimento: {data}")
print(f"Tempo de serviço: {tempo}")
if aposentadoria == "Sim":
    print("Requerer aposentadoria")
else: 
    print("Não requerer aposentadoria")