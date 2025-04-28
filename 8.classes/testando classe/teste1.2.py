
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
    #aqui são os atributos da classe
    Nome: str
    Email: str
    Telefone: int
    Endereço: str
                        #sempre que uma função usar (self) obrigatoriamente tem que estar dentro de uma classe (aqui o nome não é função e sim método)
    def exibindo_dados(self):
        print(f"\nExibindo dados: ")
        print(f" \nnome: {self.Nome} \nEmail: {self.Email} \nTelefone: {self.Telefone} \nEndereço: {self.Endereço}")


#solicitando dados
for i in range (2):
    Nome= input("Digite seu Nome: ")
    Email= input("Digite seu Email: ")
    Telefone= int(input("Digite seu Telefone: "))
    Endereço= input("Digite seu Endereço: ")
    pessoa= informações(Nome=Nome, Email=Email, Telefone=Telefone, Endereço=Endereço)  #como estou usando laço de reetição posso apenas colocar uma unica variavel e ela armazena mais de um valor( ideia tirada da minha cabeça, depois confirmo com o professor) 
    lista_pessoas.append(pessoa)
    limpar_terminal()
    time.sleep(1)

print()
#aqui eu chamo o laço de repetição usando a variavel pessoa dentro da lista q eu criei e por fim exibo os resultados chamando uma função
for pessoa in lista_pessoas:
    pessoa.exibindo_dados()
