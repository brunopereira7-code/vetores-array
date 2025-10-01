import os 
os.system("cls") 

#vetor lista
listas_novas=[]

for i in range(3):
    nota= int(input(f"Digite uma {i+1}º nota")) 
    listas_novas.append(nota)
    
# soma+=nota
soma=sum(listas_novas)



print(f"nota:{listas_novas}") 
# print(f"nota:{listas_novas[0]}") 
# print(f"nota:{listas_novas[1]}") 
# print(f"nota:{listas_novas[2]}")  

for i in range(3):
    print(f"nota {listas_novas[i]}")

print(f"nota:{listas_novas[i]}")
print(f"a soma é {soma}")
print("fim") 
