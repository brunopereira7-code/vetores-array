import os 
os.system("cls") 

numeros=[]
soma_positvos=0
quantidades_negativos=0


for i in range(5):
    numero=int(input(f"digite um numero:")) 
    numeros.append(numero)
    if numero >0:
        soma_positvos+=numero
          
    elif numero <0: 
        quantidades_negativos+=1

    else: 
        print("Digite os numeros")    
    



print(f"os numeros sao {numeros}")
print(f"as quantidades negativos sao {quantidades_negativos}")
print(f"as soma dos numeros {soma_positvos}")


# import os 
# os.system("cls")

# numeros = []
# soma_positivos = 0
# quantidade_negativos = 0

# for i in range(5):
#     numero = int(input("Digite um número: ")) 
#     numeros.append(numero)
    
#     if numero > 0:
#         soma_positivos += numero
#     elif numero < 0:
#         quantidade_negativos += 1
#     else:
#         print("Número zero não entra na contagem.")

# print(f"\nOs números digitados foram: {numeros}")
# print(f"Quantidade de números negativos: {quantidade_negativos}")
# print(f"Soma dos números positivos: {soma_positivos}")
# print("Fim")
