import requests

def pegar_cotacao(moeda_origem, moeda_destino):
    with open("moedas.txt", "r") as arquivo:
        codigo_moedas = arquivo.read().split("\n")
    if moeda_origem not in codigo_moedas:
        print("Moeda de origem não foi encontrada :/")
    if moeda_destino not in codigo_moedas:
        print("Moeda de destino não foi encontrada :/")
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)
    if requisicao:
        cotacao = requisicao.json()[moeda_origem + moeda_destino]["bid"]
        return cotacao
    else:
        print("Combinação não existente na API :/")
        return ""
    
if __name__ == "__main__":
    print(pegar_cotacao("EUR", "BRL"))
    print("o VASCO é GIGANTESCO!!!!! #oVascoSobe")