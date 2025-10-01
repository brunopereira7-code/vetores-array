import os 
os.system("cls") 

notas=[] 

for i in range(3):
    nota=int(input(f"Digite a sua nota {i+1}:"))
    notas.append(nota)


if nota >=7:
    print("Aprovado")

elif nota >= 5:
    print("Recuperaçao") 

else:
    print("Reprovado")

soma=sum(notas)
media=soma/3

print(f"sua media é {media}")
print("Fim")
