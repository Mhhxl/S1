import os
import time
from dataclasses import dataclass

# CRUD:

# Create = inserir/salvar
# Read = ler/consultar
# Update = atualizar/alterar
# Delete = excluir

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

# Lista de Funcionários
lista_funcionarios = [] 

# Criando o CRUD
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
       return True
    return False

def adicionar_funcionario(lista_funcionarios):
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    nome = input("Digite o nome do funcionário: ")
    data_de_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    funcao = input("Digite a função do funcionário: ")

    limpar_terminal()
    print("Adicionando funcionário...")
    funcionario = Funcionario(nome, data_de_nascimento, cpf, funcao)
    lista_funcionarios.append(funcionario)
    print(f"Funcionário '{nome}' adicionado com sucesso!")

def listar_funcionarios(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionários está vazia! Adicione um funcionário antes de listar.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    print("\n = Lista de Funcionários =")
    for funcionario in lista_funcionarios:
        print(f""" 
              Nome: {funcionario.nome} 
              Data de Nascimento: {funcionario.data_de_nascimento}
              CPF: {funcionario.cpf} 
              Função: {funcionario.funcao}""")
        print("----------------------------------------------------------------")

def atualizar_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionários está vazia! Adicione um funcionário antes de atualizar.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_funcionarios(lista_funcionarios)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    data_nascimento_antigo = input("Digite a data de nascimento do funcionário que deseja atualizar (DD/MM/AAAA): ")
    cpf_antigo = input("Digite o CPF do funcionário que deseja atualizar: ")
    funcao_antiga = input("Digite a função do funcionário que deseja atualizar: ")

    limpar_terminal()
    print("Atualizando funcionário...")
    time.sleep(2)
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo and funcionario.data_de_nascimento == data_nascimento_antigo and funcionario.cpf == cpf_antigo and funcionario.funcao == funcao_antiga:
            print("Funcionário encontrado!")
            print("Digite os novos dados do funcionário:\n")

            novo_nome = input("Digite o novo nome: ")
            nova_data_de_nascimento = input("Digite a nova data de nascimento (DD/MM/AAAA): ")
            novo_cpf = input("Digite o novo CPF (apenas números): ")
            nova_funcao = input("Digite a nova função do funcionário: ")

            funcionario.nome = novo_nome
            funcionario.data_de_nascimento = nova_data_de_nascimento
            funcionario.cpf = novo_cpf
            funcionario.funcao = nova_funcao

            print("Atualizando dados...")
            time.sleep(2)
            print("Dados atualizados com sucesso!")
            return
        else:    
            print(f"Funcionário '{nome_antigo}' não encontrado na lista.")

def excluir_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionários está vazia! Adicione um funcionário antes de excluir.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_funcionarios(lista_funcionarios)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ")
    data_nascimento_remover = input("Digite a data de nascimento do funcionário que deseja remover (DD/MM/AAAA): ")
    cpf_remover = input("Digite o CPF do funcionário que deseja remover: ")
    funcao_remover = input("Digite a função do funcionário que deseja remover: ")

    limpar_terminal()
    print("Removendo funcionário...")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_remover and funcionario.data_de_nascimento == data_nascimento_remover and funcionario.cpf == cpf_remover and funcionario.funcao == funcao_remover:
            lista_funcionarios.remove(funcionario)
            print(f"As informações do funcionário '{nome_remover}' foram removidas com sucesso!")
            return
        else:
            print(f"Funcionário '{nome_remover}' não encontrado na lista.")

# Criando classe para o funcionário
# Atributos: nome, data de nascimento, cpf e função
@dataclass
class Funcionario:
    nome: str
    data_de_nascimento: str
    cpf: str
    funcao: str

    def exibir_dados(self):
        print("Recebendo dados...")
        time.sleep(2)
        print("Dados recebidos com sucesso!")

def main():
    limpar_terminal()
    while True:
        print("Bem-vindo ao menu de Funcionários!\n")
        print(" = Menu Principal =")
        menu = int(input("""
    1 - Adicionar Funcionário
    2 - Listar Funcionários
    3 - Atualizar Funcionário
    4 - Remover Funcionário
    5 - Sair
        
    Digite a opção desejada:        """))
        
        match menu:
            case 1:
                adicionar_funcionario(lista_funcionarios)
            case 2:
                listar_funcionarios(lista_funcionarios)
                print("Pressione Enter para continuar...")
                input()
            case 3:
                atualizar_funcionario(lista_funcionarios)
            case 4:
                excluir_funcionario(lista_funcionarios)
            case 5:
                print("Saindo do programa...")
                time.sleep(1)
                limpar_terminal()
                return
            case _:
                print("Opção inválida! Tente novamente.")
                time.sleep(2)
                limpar_terminal()
        time.sleep(2)
        limpar_terminal()

if __name__ == "__main__":
    main()
