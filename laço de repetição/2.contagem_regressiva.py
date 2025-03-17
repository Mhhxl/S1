import os
os.system ('cls')
import time
#entrada
numero=int(input("Digite um numero pra contagem regressiva: "))

#processamento
print("CONTAGEM REGRESSIVA")
for i in range (numero, 0, -1):
    print(f"{i}") 
    time.sleep(1)

#saida
print("==FIM DO PROGRAMA==")