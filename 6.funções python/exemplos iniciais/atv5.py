import os
os.system('cls || clear')

valor = float(input('Digite o valor do produto: '))

def preco_inflacionado(valor):
    if valor < 100:
        adicional = valor * 1.10
    else:
        adicional = valor * 1.20
    return adicional

def preco_descontado(valor):
    if valor <= 100:
        desconto = valor * 0.10
    elif valor > 100:
        desconto = valor * 0.20

    valor_pagar= valor - desconto
    return valor_pagar

print(f'O valor do produto com a inflação é: {preco_inflacionado(valor)}')
print(f'O valor do produto com o desconto é: {preco_descontado(valor)}')