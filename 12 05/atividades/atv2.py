import os
os.system('cls || clear ')
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

# Lista de Alunos
lista_alunos = [] 

@dataclass
class endereco:
    logradouro :str
    numero :str
    cidade :str
    estado :str

@dataclass
class aluno:
    nome: str
    data_nascimento: str
    RA: str
    curso: str
    endereco: endereco
    



# Criando o CRUD
def verificar_lista_vazia(lista_alunos):
    if not lista_alunos:
       return True
    return False

def adicionar_aluno(lista_alunos):
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    nome = input("Digite o nome do aluno: ")
    data_de_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    curso = input("Digite o curso do aluno: ")
    endereco = input("Digite a endereço do aluno: ")

    limpar_terminal()
    print("Adicionando aluno...")
    aluno= aluno(nome, data_de_nascimento, curso, endereco)
    lista_alunos.append(aluno)
    print(f"Aluno '{nome}' adicionado com sucesso!")
    
    
def listar_alunos(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de alunos está vazia! Adicione um aluno ora  poder listar")
        return
    
    limpar_terminal()
    print("Carregando... \n")
    time.sleep(2)
    

    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    print("\n = Lista de Alunos =")
    for aluno in lista_alunos:
        print(f""" 
              Nome: {aluno.nome} 
              Data de Nascimento: {aluno.data_nascimento}
              Curso: {aluno.curso} 
              Endeeço: {aluno.endereco}""")
        print("----------------------------------------------------------------")

def atualizar_alunos(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de alunos está vazia! Adicione um aluno antes de atualizar.")
        return
        
        
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_alunos(lista_alunos)
    nome_antigo = input("Digite o nome do Aluno que deseja atualizar: ")
    data_nascimento_antigo = input("Digite a data de nascimento do Aluno que deseja atualizar (DD/MM/AAAA): ")
    curso_antigo = input("Digite o CPF do Aluno que deseja atualizar: ")
    endereco_antigo = input("Digite a função do Aluno que deseja atualizar: ")

    limpar_terminal()
    print("Atualizando Aluno...")
    time.sleep(2)
    for aluno in lista_alunos:
        if aluno.nome == nome_antigo and aluno.data_nascimento == data_nascimento_antigo and aluno.curso == curso_antigo and aluno.endereco == endereco_antigo:
            print("Aluno encontrado!")
            print("Digite os novos dados do Aluno:\n")

            novo_nome = input("Digite o novo nome: ")
            nova_data_nascimento = input("Digite a nova data de nascimento (DD/MM/AAAA): ")
            novo_curso = input("Digite o novo curso: ")
            novo_endereco    = input("Digite a nova função do Aluno: ")

            aluno.nome = novo_nome
            aluno.data_nascimento = nova_data_nascimento
            aluno.cpf = novo_curso
            aluno.funcao = novo_endereco    

            print("Atualizando dados...")
            time.sleep(2)
            print("Dados atualizados com sucesso!")
            return
        else:    
            print(f"Aluno '{nome_antigo}' não encontrado na lista.")
        
        
        
def excluir_aluno(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de funcionários está vazia! Adicione um aluno antes de excluir.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_alunos(lista_alunos)
    nome_remover = input("Digite o nome do aluno que deseja remover: ")
    data_nascimento_remover = input("Digite a data de nascimento do aluno que deseja remover (DD/MM/AAAA): ")
    curso_remover = input("Digite o curso do aluno que deseja remover: ")
    endereco_remover = input("Digite o endereço do aluno que deseja remover: ")

    limpar_terminal()
    print("Removendo aluno...")
    for aluno in lista_alunos:
        if aluno.nome == nome_remover and aluno.data_nascimento == data_nascimento_remover and aluno.curso == curso_remover and aluno.endereco == endereco_remover:
            lista_alunos.remove(aluno)
            print(f"As informações do aluno '{nome_remover}' foram removidas com sucesso!")
            return
        else:
            print(f"Aluno '{nome_remover}' não encontrado na lista.")
            
def main():
    limpar_terminal()
    while True:
        print("Bem-vindo ao menu de Alunos!\n")
        print(" = Menu Principal =")
        menu = int(input("""
    1 - Adicionar Aluno 
    2 - Listar Alunos
    3 - Atualizar Aluno 
    4 - Remover Aluno   
    5 - Sair
        
    Digite a opção desejada:        """))
        
        match menu:
            case 1:
                adicionar_aluno(listar_alunos)
            case 2:
                listar_alunos(listar_alunos)
                print("Pressione Enter para continuar...")
                input()
            case 3:
                atualizar_alunos(listar_alunos)
            case 4:
                excluir_aluno(listar_alunos)
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

