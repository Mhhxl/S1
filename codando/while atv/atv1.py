import os
os.system('cls')

#entrada

#processamento
while True:
    nota1= int(input("Digite sua nota: "))

    if nota1 < 0 or nota1 > 10:
        print("Repetindo...")
    else:
        break


#saida
print(f"A nota do aluno é {nota1}")


#primeira atividade e eu nem sei por onde começar, revisar esse assunto e o "for" quando chegar em casa
#foi mais fácil doq eu pensei(meu erro foi ter colocado a 'pergunta' fora do comando while true)