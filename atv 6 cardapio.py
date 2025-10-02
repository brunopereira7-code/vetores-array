import os 
os.system("cls") 

menu={ 
    "1 picanha": 25.00,
    "2 Lasanha": 20.00, 
    "3 Strogonoff": 18.00,
    "4 Bife Acebolado": 15.00,
    "5 Pao com ovo": 5.00,    
} 

print("-----------Cardapio---------")

total_conta=0.0
pratos_pedidos=[]

for prato,preco in menu .items():
    print(f"{prato:<20} R$ {preco:>6.2f}") 

try:
    quantidades_pratos=int(input("digite o prato quantos quer?"))
except ValueError:
    print("quantidade invalida por favor digite apenas numero") 
    quantidades_pratos=0

for i in range(quantidades_pratos):
    prato_escolhido=input(f"digite o nome do {i+1}º prato:").lower().strip() 

if prato_escolhido in menu:
    preco_do_prato=menu[prato_escolhido] 
    total_conta += preco_do_prato 

    pratos_pedidos.append(prato_escolhido)
    print(f"{prato_escolhido} adicionado a pedido custo R$ { preco_do_prato:.2f}")
else:
    print(f"desculpa o prato {prato_escolhido} nao ta no cardapio tente novamente")

print("=============Resumo do pedido===========")
for prato in pratos_pedidos:
    print(f"os pratos que voce pediu foram {','.join(pratos_pedidos)}")
    print(f"o total da conta é R$ {total_conta:.2f}")
    print("========================")

