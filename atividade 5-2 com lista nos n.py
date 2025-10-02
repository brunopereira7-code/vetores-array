import os 
os.system("cls") 

listas_numeros=[]
vetor_numeros=6

quantidade_pares=[]
quantidade_impares=[]

maior=max(listas_numeros)
menor=min(listas_numeros) 

for i in range(vetor_numeros):
    numero=int(input(f"Digite o numero {i+1}:"))
    listas_numeros.append(numero) 
    if numero % 2 == 0:
        quantidade_pares.append(numero)
    else:
        quantidade_impares.append(numero)

# for i in range(vetor_numeros):
#     print(f"os numeros sao {listas_numeros[i]}")

#ForEach-para cada
for numero in listas_numeros:
    print(f"numero é {numero}")
 
print(f"maior numero é {maior}")
print(f"menor numero é {menor}")
print(f"quantidade de numeros  pares é {quantidade_pares}")
print(f"quantidade de numeros impares é {quantidade_impares}") 
