import os
os.system("cls") 

#funçao com passagem de parametros
#criando uma funçao
def saudacao(nome,idade,altura,peso):
    print(f"ola, {nome}! Bem-vindo(a)!") 
    print(f"sua idade é {idade} anos") 
    print(f"sua peso é {peso} KG") 
    print(f"sua altura é {altura} Metros ") 

#solicitando dados
nome=input("digite seu nome:")
idade=int(input("Digite sua idade:")) 
peso=float(input("Digite seu peso:")) 
altura=float(input("Digite sua altura:")) 

#chamando a funçao 
saudacao(nome,idade,altura,peso) 

