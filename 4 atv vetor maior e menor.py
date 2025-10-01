import os 
os.system("cls") 

numero=[] 

for i in range(5):
    numeros=int(input("digite o numero:"))
    numero.append(numeros)

maior=max(numero)
menor=min(numero)


for i in range(5):
    print(f"os  numeros foram:numero{[i]}")


print(f"o maior numero é {maior}")
print(f"o menor numero é {menor}")

