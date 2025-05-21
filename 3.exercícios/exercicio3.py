import os
os.system("clear")

print("SEJA BEM VINDO")

primeiro_numero=int(input("DIGITE O PRIMEIRO NUMERO: "))
segundo_numero=int(input("DIGITE O SEUGNDO NÚMERO: "))
 
soma = primeiro_numero + segundo_numero
produto= primeiro_numero * segundo_numero
media= soma / 2

print(f"SOMA: {soma}")
print(f"MÉDIA: {media}")
print(f"PRODUTO: {produto}")

if primeiro_numero > segundo_numero:
    print(f"Primeiro numero {primeiro_numero:}, é maior do que o segundo numero {segundo_numero}")
elif primeiro_numero == segundo_numero:
    print(f"O Segundo numero {segundo_numero:}, é igual ao primeiro numero {primeiro_numero:}")
else:
    print(f"O segundo numero {segundo_numero:}, é maior que o primeiro numero {primeiro_numero:}")


#SEGUNDA FORMA DE FAZER UM NUMERO MAIOR DOQUE OUTRO
# menor= min({primeiro_numero, segundo_numero})
# maior= max({primeiro_numero, segundo_numero})
 
# print(f"O maior numero é: {maior}")
# print(f"O menor numero é: {menor}")
