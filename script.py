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
    1: ("Blusa Cropped", 50),
    2: ("Calça Jeans", 120),
    3: ("Batom Duvidoso", 3),
    4: ("Paleta de Sombras", 10),
    5: ("Presilha de Cabelo", 60)
}

print("Bem-vindo às Lojas Chein!")
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
print("Obrigado por comprar nas Lojas Chein!")
