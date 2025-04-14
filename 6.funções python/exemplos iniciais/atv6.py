import os
from datetime import date
os.system('cls || clear')

ano_nascimento = int(input('Digite o ano de nascimento: '))

def idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade


print(f'A sua idade é: {idade(ano_nascimento)}')