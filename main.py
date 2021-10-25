from cotacao import pegar_cotacao

with open("produtos.txt", "r") as arquivo:
    lista_precos = arquivo.read().split("\n")

for linha in lista_precos:
    produto, valor, moeda = linha.split(",")
    cotacao = pegar_cotacao(moeda, "BRL")
    print(f"{produto} está custando R${float(cotacao) * float(valor): ,.2f} hoje!")