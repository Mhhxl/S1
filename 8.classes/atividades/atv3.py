import os
os.system('cls || clear')
from dataclasses import dataclass

nome= (input("Digite seu nome: "))
idade= int(input("Digite sua idade: "))

@dataclass
class endereço():
    logradouro : str
    numero : int
    cidade: str

@dataclass
class informações():
    Nome: str
    Email: str
    endereço : endereço
    def exibir_dados(self):
        print(f"""Nome: {self.Nome}
              Email: {self.Email}
                Endereço: {endereço.numero}""")
        
