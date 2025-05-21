import os
os.system ("clear")

print("SEJA BEM VINDO")
nota_um=float(input("DIGITE SUA PRIMEIRA NOTA: "))
nota_dois=float(input("DIGITE SUA SEGUNDA NOTA: "))
nota_tres=float(input("DIGITE SUA TERCEIRA NOTA: "))

soma= nota_um+nota_dois+nota_tres
media= soma / 3

print(f"MÉDIA FINAL: {media}")
#meu erro foi colocar a variavel fora das aspas
if media < 7:
    print("REPROVADO")
else:
    print("APROVADO")