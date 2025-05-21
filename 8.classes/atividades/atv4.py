import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Funcionario:
    #Atributos: são variaveis que pertence a classe
    nome: str
    data_admissao: int
    matricula: int
    endereço: str

#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    
    def dados_funcionario (self):
        print (f"Nome: {self.nome} \nData de admissão: {self.data_admissao}\nMatrícula: {self.matricula}\nEndereço: {self.endereço}\n ")
lista_pessoas= []
data_admissao = int(input("Digite a data que você entrou na empresa: " )),
matricula = int(input("Digite sua matrícula: ")),
endereço = input("Digite seu endereço: ")
QUANTIDADE_PESSOAS = 3

#Atribuindo dados ao paciente1.
for i in range (QUANTIDADE_PESSOAS):
    funcionario = Funcionario(
                        nome= input("Bem vindo, funcionário! Digite seu nome : "),
                    )
    lista_pessoas.append(funcionario)


#Exibindo dados da pessoa.
print("\nExibindo dados.")
for funcionario in lista_pessoas:
    funcionario.dados_funcionario()

print("\n --Salvando dados do funcionário--")
#Salvando em um arquivo .txt
nome_arquivo = "Funcionário.txt"
with open (nome_arquivo, "w") as dados_do_funcionário:
    dados_do_funcionário.write(f"Nome: {funcionario.nome}\nData de admissão: {funcionario.data_admissao}\nMatrícula: {funcionario.matricula}\nEndereço: {funcionario.endereço}")
#-------------------------------------------------------------------------------------
@dataclass
class Cliente:
    nome: str
    endereço: str
    data_nascimento:int

    def dados_cliente (self):
        print (f"Nome: {self.nome} \nData de nascimento: {self.data_nascimento}\nEndereço: {self.endereço}\n ")
lista_clientes= []
QUANTIDADE_CLIENTES = 3

for i in range (QUANTIDADE_CLIENTES):
    cliente = Cliente(
                        nome= input("Bem vindo, cliente! Digite seu nome : "),
                        data_nascimento = int(input("Digite sua data de nascimento: " )),
                        endereço = input("Digite seu endereço: ")
                    )
    lista_clientes.append(cliente)


#Exibindo dados da pessoa.
print("\nExibindo dados.")
for cliente in lista_clientes:
    cliente.dados_cliente()

print("\n --Salvando dados do cliente--")
#Salvando em um arquivo .txt
nome_dados = "Cliente.txt"  
with open (nome_dados, "w") as dados_do_cliente:
    dados_do_cliente.write(f"Nome: {cliente.nome}\nData de nascimento: {cliente.data_nascimento}\nEndereço: {cliente.endereço}")

