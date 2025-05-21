import os
os.system('cls || clear')
import time
from dataclasses import dataclass
#criar um programa usando uma classe

#definindo classe
@dataclass
class humano():
    nome: str
    idade: int
    peso: float
    altura: float

#solicitando dados
nome=str(input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))


pessoa1= humano ("marcos", 18, 80.05, 1.64)
pessoa2= humano ("Débora", 19, 60, 1.50)

print("\nExibindo dados:")
print(f"\nnome: {pessoa1.nome} \nidade: {pessoa1.idade} \npeso: {pessoa1.peso} \naltura: {pessoa1.altura}")
time.sleep(2)

print(f"\nnome: {pessoa2.nome} \nidade: {pessoa2.idade} \npeso: {pessoa2.peso} \naltura: {pessoa2.altura}")
print()
print("==FIM DO PROGRAMA==")