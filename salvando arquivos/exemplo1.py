import os
os.system('cls || clear')
from dataclasses import dataclass

#função pra limpar terminal
def limpar_terminal():
    os.system('cls || clear')




#criando lista de livros
quantidade_livros= 2
lista_livros=[]

@dataclass
class Livros:
    Nome : str
    Autor : str
    Categoria : str
    Preço : float

    def exibir_dados(self):
        print(f"Nome: {self.Nome} \nAutor : {self.Autor} \nCategoria : {self.Categoria} \nPreço : {self.Preço}")



for i in range(quantidade_livros):
    livros = Livros(
        Nome= input("Digite o nome do livro: "),
        Autor=input("Digite o nome do autor deste livro: "),
        Categoria=input("Digite qual a categoria deste livro:"),
        Preço=float(input("Digite o valor deste livro: ")),
        )   
    lista_livros.append(livros)
    print()
    limpar_terminal()
#criando arquivo pra armazenar essas informações
nome_arquivo= "Catálogo de livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for livros in lista_livros:
        arquivo_livros.write(f"\n{livros.Nome} \n{livros.Autor} \n{livros.Categoria} \n{livros.Preço}")
        





