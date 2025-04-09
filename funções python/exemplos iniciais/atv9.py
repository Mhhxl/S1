import os
os.system('cls || clear')

#pedindo ao usuario suas informações de peso e alura
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
#função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc
                  
if calcular_imc (peso, altura) < 18.5:
    print('Abaixo do peso')
elif calcular_imc (peso, altura) < 24.9:
    print('Peso normal')
elif calcular_imc (peso, altura) < 29.9:
    print('Sobrepeso')
elif calcular_imc (peso, altura) < 34.9:
    print('Obesidade grau 1')
elif calcular_imc (peso, altura) < 39.9:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')
#resultado do IMC (abaixo do peso, peso normal, sobrepeso, obesidade)
print(f'O seu IMC é: {calcular_imc(peso, altura)}')