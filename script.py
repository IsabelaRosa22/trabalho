def calcular_total(items):
    total = 0
    for item in items:
        total += item[1]
    return total

def aplicar_desconto(total):
    if total >= 200:
        return total * 0.9  # 10% de desconto para compras acima de 200
    elif total >= 100:
        return total * 0.95  # 5% de desconto para compras acima de 100
    else:
        return total

produtos = {
    1: ("Vestido Floral", 50),
    2: ("Blusa Cropped", 30),
    3: ("Calça Jeans", 40),
    4: ("Bolsa de Couro", 25),
    5: ("Sapato de Salto", 60)
}

print("Bem-vindo à loja Shein!")
print("Produtos disponíveis:")
for codigo, produto in produtos.items():
    print(f"{codigo}: {produto[0]} - R${produto[1]}")

carrinho = []
continuar_comprando = "s"

while continuar_comprando.lower() == "s":
    codigo_produto = int(input("Digite o código do produto desejado: "))
    if codigo_produto in produtos:
        carrinho.append(produtos[codigo_produto])
    else:
        print("Código de produto inválido!")

    continuar_comprando = input("Deseja continuar comprando? (s/n): ")

total_compra = calcular_total(carrinho)
total_com_desconto = aplicar_desconto(total_compra)

print("\nResumo da compra:")
for produto in carrinho:
    print(f"{produto[0]} - R${produto[1]}")

print(f"\nTotal da compra: R${total_compra:.2f}")
print(f"Total com desconto: R${total_com_desconto:.2f}")
print("Obrigado por comprar na Shein!")
