import os
os.system("cls")

# DICIONÁRIO CORRIGIDO: chaves simplificadas e em minúsculo
menu = {
    "picanha": 25.00,
    "lasanha": 20.00,
    "strogonoff": 18.00,
    "bife acebolado": 15.00,
    "pao com ovo": 5.00,
}

print("-----------Cardapio---------")

total_conta = 0.0
pratos_pedidos = []

# Exibindo o cardápio formatado (já estava bom!)
for prato, preco in menu.items():
    print(f"{prato.title():<20} R$ {preco:>6.2f}")

try:
    quantidades_pratos = int(input("\nDigite quantos pratos diferentes você quer? "))
except ValueError:
    print("Quantidade inválida. Por favor, digite apenas um número.")
    quantidades_pratos = 0

# LOOP DE PEDIDOS
for i in range(quantidades_pratos):
    # O input agora está dentro do loop junto com a verificação
    prato_escolhido = input(f"Digite o nome do {i+1}º prato: ").lower().strip()

    # INDENTAÇÃO CORRIGIDA: if/else está dentro do loop
    if prato_escolhido in menu:
        preco_do_prato = menu[prato_escolhido]
        total_conta += preco_do_prato
        pratos_pedidos.append(prato_escolhido)
        print(f"'{prato_escolhido.title()}' adicionado ao pedido. Custo R$ {preco_do_prato:.2f}\n")
    else:
        print(f"Desculpe, o prato '{prato_escolhido}' não está no cardápio. Tente novamente.\n")

# RESUMO FINAL CORRIGIDO: fora de qualquer loop
if total_conta > 0:
    print("=============Resumo do pedido===========")
    # Usamos .title() para deixar os nomes mais bonitos na exibição
    pratos_formatados = [prato.title() for prato in pratos_pedidos]
    print(f"Os pratos que você pediu foram: {', '.join(pratos_formatados)}")
    print(f"O total da conta é R$ {total_conta:.2f}")
    print("========================================")
else:
    print("\nNenhum pedido foi realizado.")