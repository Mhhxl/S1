
import os
os.system('cls || clear')
from dataclasses import dataclass
import time 

#função pra limpar terminal
def limpar_terminal():
    os.system('cls || clear')








#função pra ler os dados do usuario
#criando lista de funcionarios
lista_funcionarios = []
QUANTIDADE_FUNCIONARIOS =  5


@dataclass
class Informacoes:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n Data de Nascimento: {self.data_nascimento}\n RG: {self.rg}\n CPF: {self.cpf}")
        
        

for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario=Informacoes(
    nome = input("Digite seu nome: "),
    data_nascimento= input("Digite sua data de nascimento: "),
    rg = (input("Digite seu RG: ")),
    cpf= (input("Digite seu CPF: ")),
    )
    limpar_terminal()
    time.sleep(1)
    lista_funcionarios.append(Informacoes)

time.sleep(1)
print()
print("Exibindo dados...")
time.sleep(2)
    


#função  pra salvar os dados do usuario em um arquivo TXT
nome_arquivo = "Funcionários.txt"
with open(nome_arquivo, "a") as arquivo_funcionarios:
    for funcionario in lista_funcionarios:
        arquivo_funcionarios.write(f"""
            Nome: {funcionario.nome}
            Data de Nascimento: {funcionario.data_nascimento}
            RG: {funcionario.rg}
            CPF: {funcionario.cpf}
""")
for funcionario in lista_funcionarios:
    funcionario.exbir_dados()
    
#função pra ler os dados do usuario
try:
    with open(nome_arquivo, "r", encoding= "utf-8" ) as arquivo_funcionarios:
        linha = arquivo_funcionarios.readline()
        limpar_terminal()
        for linha in arquivo_funcionarios:
            print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado")