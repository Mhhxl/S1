import os
os.system('clear')


contador= 0
continua= "s"

while continua == 's':
    print("Repetindo...")

    contador += 1 

    continua=input("Tecla 's' se deseja continuar: ").strip().lower()
 
 
 
if contador == 0:
    print("O bloco não foi repetido")
else:
    print(f"O bloco foi repetido {contador}")

    