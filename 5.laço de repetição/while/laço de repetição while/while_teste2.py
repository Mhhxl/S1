import os
os.system('clear')


contador= 0
continua= "s"

while True:
    print("Repetindo...")


    continua=input("Tecla 's' se deseja continuar: ").strip().lower()
    contador += 1 
    if continua != 's':
        break
 
 
if contador == 0:
    print("O bloco não foi repetido")
else:
    print(f"O bloco foi repetido {contador}")

