import os
os.system('cls || clear')
from dataclasses import dataclass
import time

#função pra limpar o terminal
def limpar_terminal():
    os.system('cls || clear')
    


#criando lista de livro / quantidde de livros
QUANTIDADE_LIVROS = 2

lista_livros = []


#criando as 2 classes
@dataclass
class Autor:
    nome : str
    biografia :str
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    def exibir_detalhes(self):
        print(f"Nome : {self.autor.nome}\n Biografia: {self.autor.biografia}\n Título: {self.titulo}\n Ano: {self.ano}\n ")
        
        

for i in range(QUANTIDADE_LIVROS):
    print("Preenchendo Dados:")
    autor= Autor(
        nome=input("Digite o nome do autor: "),
        biografia=input("Digie a Biografia do autor: "),
        
    )
    livro= Livro(
        titulo=input("Digite o Título do livro: "),
        ano=int(input("Digite o ano deste livro:")),
        autor = autor
    
    )
    limpar_terminal()
    time.sleep(2)
    lista_livros.append(livro)  
    
time.sleep(1)
print()
print("Exibindo dados....")
time.sleep(2)
for livro in lista_livros:
    livro.exibir_detalhes()
    

#salvando arquivos em TXT
nome_arquivo= "Catálogo de Livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"""
 Autor: {livro.autor.nome}
 Biografia: {livro.autor.biografia}
Título: {livro.titulo}
Ano: {livro.ano}
""")

print()
