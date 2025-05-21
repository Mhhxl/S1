print("BEM-VINDO")

nome=str(input("Digite o seu nome: "))
idade=int(input("Digite a sua idade: "))
altura=float(input("Digite a sua altura: "))
#O comando (input) armazena valores somente em texto, mas qnd especificamos o tipo de dados que quero "str,int e float" o comando passa a armazenar valores numericos tambem
#O comando (int) serve para armazenar valores numericos inteiros
#O comando (float) serve para armazenar valores numericos decimais
if idade < 10:
    print("Acesso Negado!")
elif idade <18:
    print("Só daqui a um tempo garoto")
#o comando (Elif) deve ser usado como um ("caso não seja esse") e o (else) como um ("senao for nenhum dos dois") quando tiver 3 opções 
else: print("Acesso Permitido")

# print(f"Seu nome é{nome}")  
#o f dentro do parenteses e fora das aspas, significa (formatação) usado quando quero especificar a variavel usada dentro dos {}

#ANOTAÇÕES:
#Assim que possivel, entender o funcionamento dos proximos comandos para facilitar meu avanço nas aulas