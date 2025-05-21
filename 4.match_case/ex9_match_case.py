import os
os.system('clear')

#entrada de dados

nome=input('Digite o nome do aluno: ')
nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=float(nota1+nota2)/2
#conceito_A = ("< or = 9")
#conceito_C = (" > or = 7.5 and < 9")
#conceito_B = (" > or = 6 and < 7.5")
#conceito_D = (" > or = 4 and < 6")
#conceito_E = (" < 4")

#processamento de dados
print(f"média do aluno: {media}")

if media >= 9:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
else:   
      media < 4
      conceito = 'E'
print(f"conceito do aluno: {conceito}")
#saida de dados
match conceito:
    case "A" | "B" | "C":
        print('O aluno {} foi aprovado'.format(nome))
    case "D" | "E":
        print('O aluno {} foi reprovado'.format(nome))
    case _:
        print('Conceito inválido')
