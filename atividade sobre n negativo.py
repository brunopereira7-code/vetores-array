


import os 
os.system("cls") 

lista_numeros=[] 
print("solicitando numeros") 

for i in range(5):
    numero=int(input("digite o numero:"))
    if numero < 0:
        numero=0
    lista_numeros.append(numero) 

print("\n exibindo numeros") 

for i, numero in  enumerate(lista_numeros,start=1):
    print(f"{i+1} numero :{numero}") 
