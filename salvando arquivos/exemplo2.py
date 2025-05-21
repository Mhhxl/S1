import os
os.system('cls || clear')
from dataclasses import dataclass


#função pra limpar terminal
def limpar_terminal():
    os.system('cls || clear')

#criando lista de livros
quantidade_pessoas= 2
lista_pessoas=[]


@dataclass
class informações:
    Nome : str
    Data_nascimento : str
    RG : str
    CPF : float

    def exibir_dados(self):
        print(f"Nome: {self.Nome} \nData de Nascimento : {self.Data_nascimento} \nRG : {self.RG} \nCPF : {self.CPF}")




for i in range(quantidade_pessoas):
    pessoas = informações(
        Nome= input("Digite seu nome: "),
        Data_nascimento=input("Digite a sua data de nascimento "),
        RG=input("Digite Seu RG: "),
        CPF=float(input("Digite o Seu CPF: ")),
        )   
    lista_pessoas.append(informações)
    print()
    limpar_terminal()

#criando arquivo pra armazenar essas informações
nome_arquivo= "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for informações in lista_pessoas:
        nome_arquivo.write(f"\n{informações.Nome}\n {informações.Data_nascimento}\n {informações.RG}\n {informações.CPF}")
        