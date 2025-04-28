import os
os.system('cls || clear')
from dataclasses import dataclass
import time

def limpar_terminal():
    os.system('cls || clear')


#criando vetor da lista de pessoas
lista_pessoas= []

@dataclass
class informações():
    Nome: str
    Email: str
    Telefone: int
    Endereço: str

    def exibindo_dados(self):
        print(f"\nExibindo dados: ")
        print(f" \nnome: {self.Nome} \nEmail: {self.Email} \nTelefone: {self.Telefone} \nEndereço: {self.Endereço}")


#solicitando dados
for i in range (2):
    Nome= input("Digite seu Nome: ")
    Email= input("Digite seu Email: ")
    Telefone= int(input("Digite seu Telefone: "))
    Endereço= input("Digite seu Endereço: ")
    pessoa= informações(Nome=Nome, Email=Email, Telefone=Telefone, Endereço=Endereço)  
    lista_pessoas.append(pessoa)
    limpar_terminal()
    time.sleep(1)

print()

for pessoa in lista_pessoas:
    pessoa.exibindo_dados()

