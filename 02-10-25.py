import os 
os.system("cls") 

vetor_notas=[] 

for i in range(3):
    nota=float(input("digite sua nota:")) 
    vetor_notas.append(nota)

print("Monstrando notas") 

for i in range(3):
    print(f"nota {vetor_notas[i]}")