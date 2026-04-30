try:
    valorUni = float(input("Digite o valor do produto: \n"))
    quantidade = int(input("Digite a quantidade que irá comprar: \n"))
    total = valorUni * quantidade
    print(f"O valor total foi de {total}")
except:
    print("Valor inválido")
