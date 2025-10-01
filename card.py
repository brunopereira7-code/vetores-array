import os 
os.system("cls") 

# Usar um dicionário para o cardápio é muito mais organizado e fácil de usar!
cardapio = {
    "picanha": 25.00,
    "lasanha": 20.00,
    "strogonoff": 18.00,
    "bife acebolado": 15.00,
    "pao com ovo": 5.00
}

# Imprime o cardápio de forma organizada
print("----- CARDÁPIO -----")
for prato, preco in cardapio.items():
    # .capitalize() deixa a primeira letra maiúscula
    # :<20 alinha o texto à esquerda com 20 espaços
    # :>6.2f formata o preço com 2 casas decimais
    print(f"{prato.capitalize():<20} R$ {preco:>6.2f}")
print("--------------------")

# Variáveis para guardar o total da conta e a lista de pratos pedidos
total_conta = 0.0
pratos_pedidos = []

# Tratamento de erro para garantir que o usuário digite um número
try:
    # 1. Corrigido: Converter o input para um número inteiro (int)
    quantidade_pratos = int(input("Quantos pratos gostaria de pedir? "))
except ValueError:
    print("Quantidade inválida. Por favor, digite apenas números.")
    quantidade_pratos = 0 # Encerra o programa se a quantidade for inválida

# 2. Corrigido: O loop agora roda a quantidade exata de vezes que o usuário pediu
for i in range(quantidade_pratos):
    # Pede um prato por vez, dentro do loop
    prato_escolhido = input(f"Digite o nome do {i+1}º prato: ").lower().strip()

    # Verifica se o prato escolhido existe nas chaves do nosso dicionário 'cardapio'
    if prato_escolhido in cardapio:
        # 3. Corrigido: Soma o PREÇO do prato ao total da conta
        preco_do_prato = cardapio[prato_escolhido]
        total_conta += preco_do_prato # O mesmo que total_conta = total_conta + preco_do_prato
        
        # 4. Corrigido: Adiciona o prato escolhido a uma lista, para não perder os pedidos
        pratos_pedidos.append(prato_escolhido.capitalize())
        print(f"{prato_escolhido.capitalize()} adicionado ao pedido! Custo: R$ {preco_do_prato:.2f}\n")
    else:
        print(f"Desculpe, o prato '{prato_escolhido}' não está no cardápio. Tente novamente.\n")

# Imprime o resultado final depois que o loop terminar
print("\n========== RESUMO DO PEDIDO ==========")
print(f"Os pratos que você pediu foram: {', '.join(pratos_pedidos)}")
print(f"O valor total da sua conta deu: R$ {total_conta:.2f}")
print("====================================")