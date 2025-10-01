import os 
os.system("cls")

notas=[] 
nota=0

for i in range(3):
    nota_=int(input(f"digite a nota {i+1}:"))
    notas.append(nota_)

soma=sum(notas)
media=soma/3

for i in range(3):
    print(f"nota: {notas[i]}")

print(f"sua nota é {notas}")
print(f"sua media é {media:.2f}")

