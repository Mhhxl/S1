import os
os.system('cls || clear')
from dataclasses import dataclass


#criando lista de funcionarios
lista_funcionarios= []

#função pra verificar se a lista está vazia
def verificar_lista_funcionarios_vazia(lista_funcionarios):
    if not lista_funcionarios:
        return True
    return False

#função pra adicionar
def adicionar_nomes_funcionarios(lista_funcionarios):
    nome = input("Digite o nome de um funcionario:  ")
    lista_funcionarios.append()


#função pra mostrar todos os funcionarios
def listar_nomes(lista_funcionarios):
    if verificar_lista_funcionarios_vazia(lista_funcionarios):
        print("A lista está vazia! Adicione um funcionario antes de listar. ")
        return
    
    print("\n = lista de nomes =")
    for funcionario in lista_funcionarios:
        print(f"- {funcionario}")
        
#funcção pra atualizar o nome 
def atualizar_nome(lista_funcionarios):
    if verificar_lista_funcionarios_vazia(lista_funcionarios):
        print("A lista está vazia! Adicione um funcionario antes de atualizar")
        return
    lista_funcionarios(lista_funcionarios)
    nome_antigo= input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_funcionarios:
        novo_nome = input("Digite o novo nome: ")
        indice = lista_funcionarios.index(nome_antigo)
        lista_funcionarios[indice] = novo_nome
        print(f"Nome '{nome_antigo}' atualizado para '{novo_nome}' com sucesso")
    else:
        print(f"Nome '{nome_antigo} não foi encontrado na lista'")
    
    
    
#função pra excluir
def excluir_funcionario(lista_funcionarios):
    if verificar_lista_funcionarios_vazia(lista_funcionarios):
        print("A lista está vazia! Adicione um nome antes de excluir")
        return
    lista_funcionarios(lista_funcionarios)
    nome_remover = input("Digite o nome que quer remover: ")
    if nome_remover in lista_funcionarios:
        lista_funcionarios.remove(nome_remover)
        print(f"O nome '{nome_remover}' Removido com sucesso! ")
    else:
        print(f"O nome '{nome_remover}' não encontrado na lista!")
        

#criando função pra limpar terminal
def limpar_terminal():
    os.system('cls || clear ')

#adicionando a classe funcionario 
@dataclass
class funcionario: 
    nome: str
    data_nascimento : str
    cpf: str
    função : str

#criando o menu que o usuario irá interagir    


while True:
    menu_funcionario = int(input("""
            Código || Ação 
            1   || Adicionar nome
            2   || Adicionar Data de Nascimento
            3   || Adicionar CPF
            4   || Função na empresa
            5   || Fechar 
    """))
    match menu_funcionario:
        case 1:
            adicionar_nomes_funcionarios(lista_funcionarios)
        case 2:
            data_nascimento= input("Digite sua data de nascimento: ")
        case 3:
            cpf= input("Digite seu CPF: ")
        case 4:
            função_funcionario = input("Qual a função que você exerce na empresa?: ")
        case 5:
            break
        case _:
            print("opção inválida")
            lista_funcionarios.append()
            


            