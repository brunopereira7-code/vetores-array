import os 
os.system("cls") 

lista_notas=[] 

quantidade_notas=5

print("solicitando numeros") 

for i in range(quantidade_notas):
    nota=int(input("digite sua nota"))
    lista_notas.append(nota)

maior=max(lista_notas)
menor=min(lista_notas)

print("mostrando resultado")

for i in range(quantidade_notas):
    print(f"numero {lista_notas[i]}") 

print(f"o maior numero é {maior}")
print(f"o menor numero é {menor}")
